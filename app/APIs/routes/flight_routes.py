from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.APIs.crud import flight as crud_flight
from app.APIs.schemas import flight as schemas_flight
from app.APIs.db.connection import get_db

router = APIRouter()

@router.post("/flights/", response_model=schemas_flight.Flight)
def create_flight(flight: schemas_flight.FlightCreate, db: Session = Depends(get_db)):
    return crud_flight.create_flight(db=db, flight=flight)

@router.get("/flights/", response_model=list[schemas_flight.Flight])
def read_flights(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    flights = crud_flight.get_flights(db, skip=skip, limit=limit)
    return flights

@router.get("/flights/{flight_id}", response_model=schemas_flight.Flight)
def read_flight(flight_id: int, db: Session = Depends(get_db)):
    db_flight = crud_flight.get_flight(db, flight_id=flight_id)
    if db_flight is None:
        raise HTTPException(status_code=404, detail="Flight not found")
    return db_flight
