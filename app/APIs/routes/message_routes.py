from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crud import message as crud_message
from schemas import message as schemas_message
from db.connection import get_db

router = APIRouter()

@router.post("/messages/", response_model=schemas_message.Message)
def create_message(message: schemas_message.MessageCreate, db: Session = Depends(get_db)):
    return crud_message.create_message(db=db, message=message)

@router.get("/messages/", response_model=List[schemas_message.Message])
def read_messages(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    messages = crud_message.get_messages(db, skip=skip, limit=limit)
    return messages

@router.get("/messages/{message_id}", response_model=schemas_message.Message)
def read_message(message_id: int, db: Session = Depends(get_db)):
    db_message = crud_message.get_message(db, message_id=message_id)
    if db_message is None:
        raise HTTPException(status_code=404, detail="Message not found")
    return db_message
