from pydantic import BaseModel

class MessageBase(BaseModel):
    content: str
    user_id: int

class MessageCreate(MessageBase):
    pass

class Message(MessageBase):
    id: int

    class Config:
        orm_mode = True
