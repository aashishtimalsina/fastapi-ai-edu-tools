from fastapi import APIRouter
from app.schemas import AIRequest
from app.openai_integration import ask_gpt

router = APIRouter()

@router.post("/ask-ai/")
def ask_ai(request: AIRequest):
    response = ask_gpt(request.prompt)
    return {"response": response}
