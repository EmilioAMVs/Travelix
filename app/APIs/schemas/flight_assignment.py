from pydantic import BaseModel

class FlightAssignmentBase(BaseModel):
    flight_id: int
    assigned_user_id: int

class FlightAssignmentCreate(FlightAssignmentBase):
    pass

class FlightAssignment(FlightAssignmentBase):
    id: int

    class Config:
        orm_mode = True
