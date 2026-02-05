from groq import Groq
import json
from app.config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)

def classify_with_llm(transcript, features, language):

    prompt = f"""
You are a professional AI-generated voice detection system.

Your task is to decide whether the given speech audio is:

AI_GENERATED  → created using text-to-speech or AI voice synthesis  
HUMAN         → spoken by a real person

Language: {language}

Transcript from audio:
{transcript}

Extracted audio signal features:
- Pitch Variance: {features['pitch_variance']}
- Spectral Flatness: {features['spectral_flatness']}
- Energy Level: {features['energy']}

Important Guidelines:
- AI voices usually have very smooth pitch, minimal variations, robotic consistency, and lack natural pauses.
- Human voices contain natural fluctuations, breathing sounds, uneven pacing, and background imperfections.
- If pitch variance is very low and spectral flatness is high, it is more likely AI.
- If transcript sounds natural with imperfections, it is more likely HUMAN.

Based on ALL of the above information, decide carefully.

Return ONLY valid JSON in this exact format:

{{
  "classification": "AI_GENERATED or HUMAN",
  "confidenceScore": a number between 0.0 and 1.0,
  "explanation": "short technical reason for the decision"
}}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )

    try:
        result = json.loads(response.choices[0].message.content)
    except:
        result = {
            "classification": "HUMAN",
            "confidenceScore": 0.5,
            "explanation": "Unable to confidently analyze voice"
        }

    return result
