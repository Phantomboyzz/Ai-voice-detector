from fastapi import APIRouter, Depends, HTTPException
from app.schemas import VoiceRequest
from app.auth import verify_api_key

from app.utils.base64_utils import decode_base64_to_file
from app.services.language_validator import validate_language
from app.services.audio_processor import convert_to_wav
from app.services.feature_extractor import extract_audio_features
from app.services.groq_service import transcribe_audio
from app.services.llm_classifier import classify_with_llm

router = APIRouter()


@router.post("/api/voice-detection")
async def voice_detection(
    request: VoiceRequest,
    x_api_key: str = Depends(verify_api_key)
):
    try:
        validate_language(request.language)

        if request.audioFormat.lower() != "mp3":
            raise HTTPException(
                status_code=400,
                detail="Only mp3 format supported"
            )

        mp3_path = "temp_input.mp3"
        wav_path = "temp_input.wav"

        try:
            decode_base64_to_file(request.audioBase64, mp3_path)
        except Exception:
            raise HTTPException(
                status_code=400,
                detail="Invalid base64 audio data"
            )

        try:
            wav_path = convert_to_wav(mp3_path)
        except Exception:
            raise HTTPException(
                status_code=400,
                detail="Failed to process audio file – may be corrupted or unsupported"
            )

        try:
            features = extract_audio_features(wav_path)
        except Exception:
            raise HTTPException(
                status_code=400,
                detail="Could not extract features from audio – file may be too short or silent"
            )

        try:
            transcript = transcribe_audio(mp3_path)
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Transcription service failed: {str(e)}"
            )

        try:
            llm_result = classify_with_llm(
                transcript,
                features,
                request.language
            )
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Classification failed: {str(e)}"
            )

        return {
            "status": "success",
            "language": request.language,
            "classification": llm_result["classification"],
            "confidenceScore": llm_result["confidenceScore"],
            "explanation": llm_result["explanation"]
        }

    except HTTPException as http_err:
        raise http_err

    except Exception as e:
        import traceback
        raise HTTPException(
            status_code=500,
            detail=f"Unexpected server error: {repr(e)}"
        )
