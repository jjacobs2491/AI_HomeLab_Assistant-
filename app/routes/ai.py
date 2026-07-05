from fastapi import APIRouter
from app.services.ai_service import ask_ai

router = APIRouter()

@router.get("/ai")
def ai(question: str):
    return ask_ai(question)