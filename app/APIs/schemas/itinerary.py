from pydantic import BaseModel

class ItineraryBase(BaseModel):
    title: str
    description: str

class ItineraryCreate(ItineraryBase):
    pass

class Itinerary(ItineraryBase):
    id: int

    class Config:
        orm_mode = True
