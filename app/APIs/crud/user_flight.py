from sqlalchemy.orm import Session
from models.user_flight import UserFlight
from schemas.user_flight import UserFlightCreate

def get_user_flight(db: Session, user_flight_id: int):
    return db.query(UserFlight).filter(UserFlight.id == user_flight_id).first()

def get_user_flights(db: Session, skip: int = 0, limit: int = 10):
    return db.query(UserFlight).offset(skip).limit(limit).all()

def create_user_flight(db: Session, user_flight: UserFlightCreate):
    db_user_flight = UserFlight(
        user_id=user_flight.user_id,
        flight_id=user_flight.flight_id
    )
    db.add(db_user_flight)
    db.commit()
    db.refresh(db_user_flight)
    return db_user_flight
