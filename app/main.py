from fastapi import FastAPI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

from app.routes import router

app = FastAPI(title="AI Generated Voice Detection API")

app.include_router(router)

@app.get("/")
async def root():
    return {"message": "AI Voice Detection API is running"}

@app.get("/debug-env")
async def debug_env():
    return {
        "API_KEY": os.getenv("API_KEY"),
        "GROQ_API_KEY": "SET" if os.getenv("GROQ_API_KEY") else "NOT SET"
    }
