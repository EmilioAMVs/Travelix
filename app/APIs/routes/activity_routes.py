from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Activity(BaseModel):
    id: int
    name: str
    description: str

@router.get("/", response_model=list[Activity])
def get_activities():
    # Reemplaza con la llamada real a la base de datos
    return [{"id": 1, "name": "Hiking", "description": "Mountain hiking."}]

@router.post("/", response_model=Activity)
def create_activity(activity: Activity):
    # Reemplaza con la llamada real a la base de datos
    return activity
