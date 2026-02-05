from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

VALID_API_KEY = "sk_test_123456789"


def test_invalid_api_key():

    response = client.post(
        "/api/voice-detection",
        headers={"x-api-key": "wrong_key"},
        json={}
    )

    assert response.status_code == 401


def test_missing_fields():

    response = client.post(
        "/api/voice-detection",
        headers={"x-api-key": VALID_API_KEY},
        json={}
    )

    assert response.status_code == 422


def test_invalid_language():

    request_data = {
        "language": "Spanish",
        "audioFormat": "mp3",
        "audioBase64": "abcd"
    }

    response = client.post(
        "/api/voice-detection",
        headers={"x-api-key": VALID_API_KEY},
        json=request_data
    )

    assert response.status_code == 400
