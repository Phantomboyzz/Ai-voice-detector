from fastapi import HTTPException
from app.config import SUPPORTED_LANGUAGES

def validate_language(language):
    if language not in SUPPORTED_LANGUAGES:
        raise HTTPException(
            status_code=400,
            detail="Unsupported language"
        )
