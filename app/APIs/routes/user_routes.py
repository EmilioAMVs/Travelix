from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class User(BaseModel):
    id: int
    name: str
    email: str

@router.get("/", response_model=list[User])
def get_users():
    # This should be replaced with actual database call
    return [{"id": 1, "name": "John Doe", "email": "john@example.com"}]

@router.post("/", response_model=User)
def create_user(user: User):
    # This should be replaced with actual database call
    return user
