from sqlalchemy.orm import Session
from models.flight import Flight
from schemas.flight import FlightCreate

def get_flight(db: Session, flight_id: int):
    return db.query(Flight).filter(Flight.id == flight_id).first()

def get_flights(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Flight).offset(skip).limit(limit).all()

def create_flight(db: Session, flight: FlightCreate):
    db_flight = Flight(
        flight_number=flight.flight_number,
        departure_date=flight.departure_date,
        destination=flight.destination
    )
    db.add(db_flight)
    db.commit()
    db.refresh(db_flight)
    return db_flight
