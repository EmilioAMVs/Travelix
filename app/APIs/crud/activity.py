from sqlalchemy.orm import Session
from app.models.activity import Activity
from app.APIs.schemas.activity import ActivityCreate

def get_activity(db: Session, activity_id: int):
    return db.query(Activity).filter(Activity.id == activity_id).first()

def get_activities(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Activity).offset(skip).limit(limit).all()

def create_activity(db: Session, activity: ActivityCreate):
    db_activity = Activity(
        name=activity.name,
        description=activity.description,
        itinerary_id=activity.itinerary_id
    )
    db.add(db_activity)
    db.commit()
    db.refresh(db_activity)
    return db_activity
