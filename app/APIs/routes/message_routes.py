from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Message(BaseModel):
    id: int
    sender_id: int
    recipient_id: int
    content: str
    timestamp: str

@router.get("/", response_model=list[Message])
def get_messages():
    # Reemplaza con la llamada real a la base de datos
    return [
        {"id": 1, "sender_id": 1, "recipient_id": 2, "content": "Hello!", "timestamp": "2024-07-15T10:00:00"},
        {"id": 2, "sender_id": 2, "recipient_id": 1, "content": "Hi there!", "timestamp": "2024-07-15T10:05:00"}
    ]

@router.post("/", response_model=Message)
def create_message(message: Message):
    # Reemplaza con la llamada real a la base de datos
    return message
