from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crud import user as crud_user
from schemas import user as schemas_user
from db.connection import get_db

router = APIRouter()

@router.post("/users/", response_model=schemas_user.User)
def create_user(user: schemas_user.UserCreate, db: Session = Depends(get_db)):
    return crud_user.create_user(db=db, user=user)

@router.get("/users/", response_model=List[schemas_user.User])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = crud_user.get_users(db, skip=skip, limit=limit)
    return users

@router.get("/users/{user_id}", response_model=schemas_user.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud_user.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
