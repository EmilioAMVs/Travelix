from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crud import itinerary as crud_itinerary
from schemas import itinerary as schemas_itinerary
from db.connection import get_db

router = APIRouter()

@router.post("/itineraries/", response_model=schemas_itinerary.Itinerary)
def create_itinerary(itinerary: schemas_itinerary.ItineraryCreate, db: Session = Depends(get_db)):
    return crud_itinerary.create_itinerary(db=db, itinerary=itinerary)

@router.get("/itineraries/", response_model=List[schemas_itinerary.Itinerary])
def read_itineraries(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    itineraries = crud_itinerary.get_itineraries(db, skip=skip, limit=limit)
    return itineraries

@router.get("/itineraries/{itinerary_id}", response_model=schemas_itinerary.Itinerary)
def read_itinerary(itinerary_id: int, db: Session = Depends(get_db)):
    db_itinerary = crud_itinerary.get_itinerary(db, itinerary_id=itinerary_id)
    if db_itinerary is None:
        raise HTTPException(status_code=404, detail="Itinerary not found")
    return db_itinerary
