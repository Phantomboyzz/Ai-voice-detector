<div align="center">

# 🎤 AI Generated Voice Detection API

### Detect AI-Generated vs Human Speech Across Indian Languages

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg?style=for-the-badge)](LICENSE)

**Built for India AI Impact Buildathon Hackathon**

[Features](#-features) • [Installation](#-installation--setup) • [API Usage](#-api-usage) • [Testing](#-testing)

</div>

---

## 🌟 Overview

A powerful REST API that detects whether a given voice recording is **AI-generated** or **Human-spoken** using advanced audio analysis and LLM classification. The system processes Base64-encoded MP3 audio files and provides detailed classification results.

### 🎯 Problem Statement

AI systems can now generate highly realistic human-like voices, making it challenging to distinguish between authentic and synthetic speech. This API provides a reliable solution to:

- ✅ Identify AI-generated voice recordings
- ✅ Verify authentic human speech
- ✅ Support multiple Indian languages
- ✅ Provide confidence scores and explanations

---

## 🌍 Supported Languages

<table>
  <tr>
    <td align="center">🇮🇳 <b>Tamil</b></td>
    <td align="center">🇬🇧 <b>English</b></td>
    <td align="center">🇮🇳 <b>Hindi</b></td>
    <td align="center">🇮🇳 <b>Malayalam</b></td>
    <td align="center">🇮🇳 <b>Telugu</b></td>
  </tr>
</table>

---

## 🛠 Tech Stack

| Category | Technology |
|----------|-----------|
| **Framework** | FastAPI |
| **Language** | Python 3.8+ |
| **Audio Processing** | Librosa, NumPy |
| **Speech-to-Text** | Groq API |
| **Classification** | Groq LLM |
| **Authentication** | API Key |

---

## 📌 Features

<table>
  <tr>
    <td>🔐 Secure API Key Authentication</td>
    <td>📊 Audio Feature Extraction</td>
  </tr>
  <tr>
    <td>🎵 Base64 MP3 Support</td>
    <td>🗣️ Speech Transcription</td>
  </tr>
  <tr>
    <td>✅ Input Validation</td>
    <td>🤖 AI/Human Classification</td>
  </tr>
  <tr>
    <td>📈 Confidence Scoring</td>
    <td>📝 JSON Responses</td>
  </tr>
</table>

---

## 📂 Project Structure

```
ai_voice_detector/
│
├── 📁 app/
│   ├── 📄 main.py                    # Application entry point
│   ├── 📄 routes.py                  # API endpoints
│   ├── 📄 auth.py                    # Authentication logic
│   ├── 📄 config.py                  # Configuration settings
│   ├── 📄 schemas.py                 # Pydantic models
│   │
│   ├── 📁 services/
│   │   ├── 📄 audio_processor.py     # Audio processing
│   │   ├── 📄 feature_extractor.py   # Feature extraction
│   │   ├── 📄 groq_service.py        # Groq API integration
│   │   ├── 📄 llm_classifier.py      # LLM classification
│   │   └── 📄 language_validator.py  # Language validation
│   │
│   └── 📁 utils/
│       └── 📄 base64_utils.py        # Base64 utilities
│
├── 📁 tests/
│   ├── 📄 test_api.py                # API tests
│   └── 📄 sample_requests.py         # Sample requests
│
├── 📄 .env                            # Environment variables
├── 📄 requirements.txt                # Dependencies
└── 📄 README.md                       # Documentation
```

---

## 🔧 Installation & Setup

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Virtual environment (recommended)

### 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/ai-voice-detector.git
cd ai-voice-detector
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

**Activate the environment:**

- **Windows:**
  ```bash
  venv\Scripts\activate
  ```

- **macOS/Linux:**
  ```bash
  source venv/bin/activate
  ```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Environment Variables

Create a `.env` file in the project root:

```env
API_KEY=sk_test_123456789
GROQ_API_KEY=your_groq_api_key
```

> ⚠️ **Important:** Never commit your `.env` file to version control!

---

## ▶️ Running the Application

### Local Development

```bash
uvicorn app.main:app --reload
```

The API will be available at:
- **API:** http://127.0.0.1:8000
- **Swagger Docs:** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc

---

## 📡 API Usage

### Endpoint

```
POST /api/voice-detection
```

### Headers

```http
x-api-key: YOUR_SECRET_API_KEY
Content-Type: application/json
```

### Request Body

```json
{
  "language": "English",
  "audioFormat": "mp3",
  "audioBase64": "BASE64_ENCODED_AUDIO_STRING"
}
```

### Success Response

```json
{
  "status": "success",
  "language": "English",
  "classification": "HUMAN",
  "confidenceScore": 0.87,
  "explanation": "Natural pitch variation and speech patterns detected"
}
```

### Error Response

```json
{
  "status": "error",
  "message": "Could not extract features from audio – file may be too short or silent"
}
```

### Example cURL Request

```bash
curl -X POST "http://127.0.0.1:8000/api/voice-detection" \
  -H "x-api-key: YOUR_SECRET_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "language": "English",
    "audioFormat": "mp3",
    "audioBase64": "YOUR_BASE64_ENCODED_AUDIO"
  }'
```

---

## 🧪 Testing

### Run All Tests

```bash
pytest
```

### Run Sample Requests

```bash
python tests/sample_requests.py
```

### Test Coverage

```bash
pytest --cov=app tests/
```

---

## 📋 Input Requirements

| Requirement | Details |
|-------------|---------|
| **Format** | MP3 only |
| **Encoding** | Base64 |
| **Files per Request** | 1 |
| **Max Duration** | 60 seconds (recommended) |
| **Languages** | Tamil, English, Hindi, Malayalam, Telugu |

---

## 🚫 Constraints & Guidelines

- ❌ Hardcoding results is **prohibited**
- ✅ Only supported languages allowed
- ✅ Use authorized APIs only (Groq)
- ✅ Follow evaluation criteria strictly

---

## 🚀 Deployment

The API can be deployed to various platforms:

<table>
  <tr>
    <td align="center">
      <img src="https://img.shields.io/badge/Render-46E3B7?style=for-the-badge&logo=render&logoColor=white" alt="Render"/>
    </td>
    <td align="center">
      <img src="https://img.shields.io/badge/Railway-0B0D0E?style=for-the-badge&logo=railway&logoColor=white" alt="Railway"/>
    </td>
    <td align="center">
      <img src="https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white" alt="AWS"/>
    </td>
  </tr>
  <tr>
    <td align="center">
      <img src="https://img.shields.io/badge/Azure-0078D4?style=for-the-badge&logo=microsoft-azure&logoColor=white" alt="Azure"/>
    </td>
    <td align="center">
      <img src="https://img.shields.io/badge/Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white" alt="Heroku"/>
    </td>
    <td align="center">
      <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker"/>
    </td>
  </tr>
</table>

### Deployment Checklist

- [ ] Set environment variables on platform
- [ ] Configure secrets securely
- [ ] Test API endpoints post-deployment
- [ ] Monitor logs and performance
- [ ] Set up error tracking

---

## 🧠 Evaluation Criteria

<table>
  <tr>
    <td>✅ <b>Accuracy</b></td>
    <td>AI vs Human detection precision</td>
  </tr>
  <tr>
    <td>🌍 <b>Multi-language</b></td>
    <td>Performance across 5 languages</td>
  </tr>
  <tr>
    <td>⚡ <b>Reliability</b></td>
    <td>API uptime and consistency</td>
  </tr>
  <tr>
    <td>📊 <b>Response Format</b></td>
    <td>JSON structure compliance</td>
  </tr>
  <tr>
    <td>💡 <b>Explanation Quality</b></td>
    <td>Clear and actionable insights</td>
  </tr>
</table>

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📞 Support

Having issues? Need help?

- 📧 Email: aryanjha326@gmail.com
- 🐛 [Report a Bug](https://github.com/Phantomboyzz/ai-voice-detector/issues)
- 💬 [Discussions](https://github.com/Phantomboyzz/ai-voice-detector/discussions)

---

## 👨‍💻 Author

**Built for India AI Impact Buildathon**

Made with ❤️ by [Aryan Jha](https://github.com/Phantomboyzz)

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">

### ⭐ Star this repository if you find it helpful!

**[Back to Top](#-ai-generated-voice-detection-api)**

</div>