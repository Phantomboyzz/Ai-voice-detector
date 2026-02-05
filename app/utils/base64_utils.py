import base64

def decode_base64_to_file(base64_string: str, file_path: str) -> str:
    try:
        audio_data = base64.b64decode(base64_string)
        with open(file_path, "wb") as f:
            f.write(audio_data)
        return file_path
    except Exception as e:
        raise ValueError("Invalid Base64 audio data")
