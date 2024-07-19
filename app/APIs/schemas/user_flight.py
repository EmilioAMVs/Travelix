from pydantic import BaseModel

class UserFlightBase(BaseModel):
    user_id: int
    flight_id: int

class UserFlightCreate(UserFlightBase):
    pass

class UserFlight(UserFlightBase):
    id: int

    class Config:
        orm_mode = True
