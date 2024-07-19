from pydantic import BaseModel
from datetime import datetime
from typing import List

class FlightBase(BaseModel):
    flight_number: str
    departure_date: datetime
    destination: str

class FlightCreate(FlightBase):
    pass

class Flight(FlightBase):
    id: int
    user_flights: List['UserFlight'] = []

    class Config:
        orm_mode = True
