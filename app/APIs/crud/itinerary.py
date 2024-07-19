from sqlalchemy.orm import Session
from models.itinerary import Itinerary
from schemas.itinerary import ItineraryCreate

def get_itinerary(db: Session, itinerary_id: int):
    return db.query(Itinerary).filter(Itinerary.id == itinerary_id).first()

def get_itineraries(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Itinerary).offset(skip).limit(limit).all()

def create_itinerary(db: Session, itinerary: ItineraryCreate):
    db_itinerary = Itinerary(
        title=itinerary.title,
        description=itinerary.description
    )
    db.add(db_itinerary)
    db.commit()
    db.refresh(db_itinerary)
    return db_itinerary
