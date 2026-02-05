import base64
from app.utils.base64_utils import decode_base64_to_file


def test_base64_decode():

    sample_text = "hello world"
    encoded = base64.b64encode(sample_text.encode()).decode()

    file_path = "test.txt"

    decode_base64_to_file(encoded, file_path)

    with open(file_path, "r") as f:
        content = f.read()

    assert content == sample_text
