from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Flight(BaseModel):
    id: int
    airline: str
    flight_number: str
    departure_time: str
    arrival_time: str

@router.get("/", response_model=list[Flight])
def get_flights():
    # Reemplaza con la llamada real a la base de datos
    return [
        {"id": 1, "airline": "Airline A", "flight_number": "AA123", "departure_time": "2024-07-15T10:00:00", "arrival_time": "2024-07-15T12:00:00"},
        {"id": 2, "airline": "Airline B", "flight_number": "BB456", "departure_time": "2024-07-15T14:00:00", "arrival_time": "2024-07-15T16:00:00"}
    ]

@router.post("/", response_model=Flight)
def create_flight(flight: Flight):
    # Reemplaza con la llamada real a la base de datos
    return flight
