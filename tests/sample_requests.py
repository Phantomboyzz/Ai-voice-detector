import base64
import json
import requests

API_URL = "http://localhost:8000/api/voice-detection"
API_KEY = "sk_test_123456789"


def create_base64_from_mp3(file_path):

    with open(file_path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()

    return encoded


def test_request(mp3_file, language):

    base64_audio = create_base64_from_mp3(mp3_file)

    payload = {
        "language": language,
        "audioFormat": "mp3",
        "audioBase64": base64_audio
    }

    headers = {
        "Content-Type": "application/json",
        "x-api-key": API_KEY
    }

    response = requests.post(
        API_URL,
        headers=headers,
        data=json.dumps(payload)
    )

    print("Status Code:", response.status_code)
    print("Response:", response.text)


if __name__ == "__main__":

    # Example usage:
    test_request("sample voice 1.mp3", "English")
