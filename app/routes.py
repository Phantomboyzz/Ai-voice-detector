from fastapi import APIRouter, Depends
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
    api_key: str = Depends(verify_api_key)
):

    validate_language(request.language)

    if request.audioFormat.lower() != "mp3":
        return {
            "status": "error",
            "message": "Only mp3 format supported"
        }

    mp3_path = "temp_input.mp3"
    decode_base64_to_file(request.audioBase64, mp3_path)

    wav_path = convert_to_wav(mp3_path)

    features = extract_audio_features(wav_path)

    transcript = transcribe_audio(mp3_path)

    llm_result = classify_with_llm(
        transcript,
        features,
        request.language
    )

    return {
        "status": "success",
        "language": request.language,
        "classification": llm_result["classification"],
        "confidenceScore": llm_result["confidenceScore"],
        "explanation": llm_result["explanation"]
    }
