from fastapi import Depends, HTTPException, status
from fastapi.security import APIKeyHeader
from app.core.config import settings
import secrets
import string
import time

# Simulación de base de datos de API Keys para el MVP
# En producción, esto debería estar en una base de datos
API_KEYS = {
    "sk-demo-key123456789": {
        "user_id": "user1",
        "rate_limit": 100,  # solicitudes por minuto
        "created_at": time.time()
    }
}

api_key_header = APIKeyHeader(name="Authorization", auto_error=False)

async def get_api_key(api_key_header: str = Depends(api_key_header)):
    if not api_key_header:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="API key missing",
        )
    
    # Verificar formato Bearer
    if not api_key_header.startswith("Bearer "):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API key format. Use 'Bearer YOUR_API_KEY'",
        )
        
    api_key = api_key_header.replace("Bearer ", "")
    
    if api_key not in API_KEYS:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API key",
        )
    
    return api_key

def generate_api_key():
    """Generate a new API key."""
    random_part = ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(24))
    return f"sk-{random_part}"