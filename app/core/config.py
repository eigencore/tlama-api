from typing import List
from pydantic import BaseSettings
import secrets
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    PROJECT_NAME: str = "TLAMA-API"
    API_V1_STR: str = "/v1"
    
    # Seguridad
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7 días
    
    # CORS
    ALLOWED_ORIGINS: List[str] = ["*"]
    
    # Base de datos
    DATABASE_URL: str = "sqlite:///./app.db"
    
    # Límites de la API
    DEFAULT_MAX_TOKENS: int = 1000
    DEFAULT_TEMPERATURE: float = 0.7
    
    # Modelos disponibles
    AVAILABLE_MODELS: List[str] = ["modelo-base", "modelo-avanzado"]
    DEFAULT_MODEL: str = "modelo-base"
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()