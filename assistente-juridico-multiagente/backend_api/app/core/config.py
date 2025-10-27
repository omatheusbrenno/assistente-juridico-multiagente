import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()

class Settings(BaseSettings):
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY")
    SERPER_API_KEY: str = os.getenv("SERPER_API_KEY")
    BACKEND_API_URL: str = os.getenv("BACKEND_API_URL", "http://backend_api:8000")

    class Config:
        case_sensitive = True

settings = Settings()