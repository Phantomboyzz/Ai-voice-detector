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
        # Validate language
        validate_language(request.language)

        # Validate format
        if request.audioFormat.lower() != "mp3":
            raise HTTPException(
                status_code=400,
                detail="Only mp3 format supported"
            )

        # Decode Base64 to MP3 file
        mp3_path = "temp_input.mp3"
        decode_base64_to_file(request.audioBase64, mp3_path)

        # Convert to WAV for processing
        wav_path = convert_to_wav(mp3_path)

        # Extract audio features
        features = extract_audio_features(wav_path)

        # Transcribe audio using Groq
        transcript = transcribe_audio(mp3_path)

        # Classify using LLM
        llm_result = classify_with_llm(
            transcript,
            features,
            request.language
        )

        # Return final structured response
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
        # Catch unexpected errors and return clean message
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
