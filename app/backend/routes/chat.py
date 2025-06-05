from fastapi import APIRouter, HTTPException, status

from app.backend.models.chat import ChatPayload, ChatResponse
from app.service.ai_engine import get_medical_response

router = APIRouter()

@router.post("/ask")
async def ask(payload: ChatPayload) -> ChatResponse:
    try:
        return await get_medical_response(question=payload.question, max_tokens=100)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))  

@router.post("/symptom")
async def symptom(payload: ChatPayload) -> ChatResponse:
    try:
        response = await get_medical_response(question=payload.question, max_tokens=200)
        
        if response==None:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.post("/disease")
async def disease(payload: ChatPayload) -> ChatResponse:
    try:
        response = await get_medical_response(question=payload.question, max_tokens=200)
        
        if response==None:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))  

@router.post("/firstaid")
async def firstAid(payload: ChatPayload) -> ChatResponse:
    try:
        response = await get_medical_response(question=payload.question, max_tokens=200)
        
        if response==None:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)) 
        