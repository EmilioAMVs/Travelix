from sqlalchemy.orm import Session
from models.message import Message
from schemas.message import MessageCreate

def get_message(db: Session, message_id: int):
    return db.query(Message).filter(Message.id == message_id).first()

def get_messages(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Message).offset(skip).limit(limit).all()

def create_message(db: Session, message: MessageCreate):
    db_message = Message(
        content=message.content,
        user_id=message.user_id
    )
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message
