from typing import List, Optional, Dict, Any, Union
from pydantic import BaseModel, Field
from app.core.config import settings

class Message(BaseModel):
    role: str = Field(..., description="El rol del autor del mensaje: 'system', 'user', o 'assistant'")
    content: str = Field(..., description="El contenido del mensaje")

class ChatRequest(BaseModel):
    model: str = Field(default=settings.DEFAULT_MODEL, description="ID del modelo a utilizar")
    messages: List[Message] = Field(..., description="Lista de mensajes en la conversación")
    temperature: float = Field(default=settings.DEFAULT_TEMPERATURE, description="Qué tan aleatorias son las respuestas")
    max_tokens: int = Field(default=settings.DEFAULT_MAX_TOKENS, description="El número máximo de tokens a generar")
    stream: bool = Field(default=False, description="Si se deben transmitir respuestas parciales")

class CompletionRequest(BaseModel):
    model: str = Field(default=settings.DEFAULT_MODEL, description="ID del modelo a utilizar")
    prompt: str = Field(..., description="El prompt para generar el texto")
    temperature: float = Field(default=settings.DEFAULT_TEMPERATURE, description="Qué tan aleatorias son las respuestas")
    max_tokens: int = Field(default=settings.DEFAULT_MAX_TOKENS, description="El número máximo de tokens a generar")

class EmbeddingRequest(BaseModel):
    model: str = Field(default=settings.DEFAULT_MODEL, description="ID del modelo a utilizar")
    input: Union[str, List[str]] = Field(..., description="El texto o textos para convertir a embeddings")