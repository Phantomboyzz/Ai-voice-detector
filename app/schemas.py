from pydantic import BaseModel

class VoiceRequest(BaseModel):
    language: str
    audioFormat: str
    audioBase64: str
