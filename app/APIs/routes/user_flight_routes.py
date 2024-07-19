from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crud import user_flight as crud_user_flight
from schemas import user_flight as schemas_user_flight
from db.connection import get_db

router = APIRouter()

@router.post("/user_flights/", response_model=schemas_user_flight.UserFlight)
def create_user_flight(user_flight: schemas_user_flight.UserFlightCreate, db: Session = Depends(get_db)):
    return crud_user_flight.create_user_flight(db=db, user_flight=user_flight)

@router.get("/user_flights/", response_model=List[schemas_user_flight.UserFlight])
def read_user_flights(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    user_flights = crud_user_flight.get_user_flights(db, skip=skip, limit=limit)
    return user_flights

@router.get("/user_flights/{user_flight_id}", response_model=schemas_user_flight.UserFlight)
def read_user_flight(user_flight_id: int, db: Session = Depends(get_db)):
    db_user_flight = crud_user_flight.get_user_flight(db, user_flight_id=user_flight_id)
    if db_user_flight is None:
        raise HTTPException(status_code=404, detail="UserFlight not found")
    return db_user_flight
