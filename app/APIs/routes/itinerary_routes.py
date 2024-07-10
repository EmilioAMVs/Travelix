from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Itinerary(BaseModel):
    id: int
    name: str
    details: str

@router.get("/", response_model=list[Itinerary])
def get_itineraries():
    # Reemplaza con la llamada real a la base de datos
    return [{"id": 1, "name": "Summer Trip", "details": "A trip to the beach."}]

@router.post("/", response_model=Itinerary)
def create_itinerary(itinerary: Itinerary):
    # Reemplaza con la llamada real a la base de datos
    return itinerary
