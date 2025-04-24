from fastapi import APIRouter, Depends, HTTPException
from app.core.security import get_api_key
from app.schemas.requests import ChatRequest
from app.schemas.responses import ChatResponse
from app.services.ai_provider import AIProvider

router = APIRouter()

@router.post("/completions", response_model=ChatResponse)
async def create_chat_completion(
    request: ChatRequest,
    api_key: str = Depends(get_api_key)
):
    """
    Crea una respuesta de chat basada en los mensajes proporcionados.
    Similar al endpoint de OpenAI /chat/completions
    """
    try:
        ai_provider = AIProvider()
        response = await ai_provider.generate_chat_response(
            messages=request.messages,
            model=request.model,
            temperature=request.temperature,
            max_tokens=request.max_tokens
        )
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))