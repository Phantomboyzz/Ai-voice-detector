import base64

with open("sample voice 1.mp3", "rb") as file:
    encoded = base64.b64encode(file.read()).decode()

print(encoded)
