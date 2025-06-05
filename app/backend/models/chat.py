from pydantic import BaseModel

class ChatPayload(BaseModel):
    user_id: str
    question: str

class ChatResponse(BaseModel):
    answer: str
