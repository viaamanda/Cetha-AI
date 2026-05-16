from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional
from pathlib import Path

class Settings(BaseSettings):
    PROJECT_NAME: str = "Cetha AI"
    VERSION: str = "0.1.0"
    API_V1_STR: str = "/api/v1"

    # Gemini API
    GEMINI_API_KEY: Optional[str] = None

    # Google Cloud Vision
    GOOGLE_APPLICATION_CREDENTIALS: Optional[str] = "gcp-credentials.json"

    # Firebase
    FIREBASE_CREDENTIALS: Optional[str] = "firebase-credentials.json"

    model_config = SettingsConfigDict(
        env_file=Path(__file__).resolve().parent.parent.parent / ".env", 
        case_sensitive=True
    )

settings = Settings()
