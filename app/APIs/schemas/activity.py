from pydantic import BaseModel

class ActivityBase(BaseModel):
    name: str
    description: str
    itinerary_id: int

class ActivityCreate(ActivityBase):
    pass

class Activity(ActivityBase):
    id: int

    class Config:
        orm_mode = True
