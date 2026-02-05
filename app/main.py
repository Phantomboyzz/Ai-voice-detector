from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="AI Generated Voice Detection API")

app.include_router(router)
