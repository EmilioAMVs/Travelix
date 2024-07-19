from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.APIs.crud import activity as crud_activity
from app.APIs.schemas import activity as schemas_activity
from app.APIs.db.connection import get_db

router = APIRouter()

@router.post("/activities/", response_model=schemas_activity.Activity)
def create_activity(activity: schemas_activity.ActivityCreate, db: Session = Depends(get_db)):
    return crud_activity.create_activity(db=db, activity=activity)

@router.get("/activities/", response_model=list[schemas_activity.Activity])
def read_activities(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    activities = crud_activity.get_activities(db, skip=skip, limit=limit)
    return activities

@router.get("/activities/{activity_id}", response_model=schemas_activity.Activity)
def read_activity(activity_id: int, db: Session = Depends(get_db)):
    db_activity = crud_activity.get_activity(db, activity_id=activity_id)
    if db_activity is None:
        raise HTTPException(status_code=404, detail="Activity not found")
    return db_activity
