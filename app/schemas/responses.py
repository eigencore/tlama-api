from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field
import time

class Choice(BaseModel):
    message: Dict[str, str] = Field(..., description="Mensaje generado")
    finish_reason: str = Field(..., description="Razón por la que la generación terminó")
    index: int = Field(0, description="Índice de la elección")

class Usage(BaseModel):
    prompt_tokens: int = Field(..., description="Número de tokens en el prompt")
    completion_tokens: int = Field(..., description="Número de tokens en la respuesta")
    total_tokens: int = Field(..., description="Número total de tokens utilizados")

class ChatResponse(BaseModel):
    id: str = Field(..., description="ID único de la respuesta")
    object: str = Field("chat.completion", description="Tipo de objeto")
    created: int = Field(default_factory=lambda: int(time.time()), description="Timestamp de creación")
    model: str = Field(..., description="ID del modelo utilizado")
    choices: List[Choice] = Field(..., description="Lista de respuestas generadas")
    usage: Usage = Field(..., description="Información de uso de tokens")

class CompletionResponse(BaseModel):
    id: str = Field(..., description="ID único de la respuesta")
    object: str = Field("text_completion", description="Tipo de objeto")
    created: int = Field(default_factory=lambda: int(time.time()), description="Timestamp de creación")
    model: str = Field(..., description="ID del modelo utilizado")
    choices: List[Dict[str, Any]] = Field(..., description="Lista de respuestas generadas")
    usage: Usage = Field(..., description="Información de uso de tokens")

class EmbeddingData(BaseModel):
    embedding: List[float] = Field(..., description="Vector de embedding")
    index: int = Field(..., description="Índice del embedding")

class EmbeddingResponse(BaseModel):
    object: str = Field("list", description="Tipo de objeto")
    data: List[EmbeddingData] = Field(..., description="Lista de embeddings")
    model: str = Field(..., description="ID del modelo utilizado")
    usage: Usage = Field(..., description="Información de uso de tokens")