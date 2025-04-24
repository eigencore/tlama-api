from fastapi import APIRouter
from app.api.v1.endpoints import chat, completions, embeddings

api_router = APIRouter()

# Incluir routers de los diferentes endpoints
api_router.include_router(chat.router, prefix="/chat", tags=["chat"])
api_router.include_router(completions.router, prefix="/completions", tags=["completions"])
api_router.include_router(embeddings.router, prefix="/embeddings", tags=["embeddings"])