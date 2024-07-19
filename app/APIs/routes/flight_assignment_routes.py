from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crud import flight_assignment as crud_flight_assignment
from schemas import flight_assignment as schemas_flight_assignment
from db.connection import get_db

router = APIRouter()

@router.post("/flight_assignments/", response_model=schemas_flight_assignment.FlightAssignment)
def create_flight_assignment(flight_assignment: schemas_flight_assignment.FlightAssignmentCreate, db: Session = Depends(get_db)):
    return crud_flight_assignment.create_flight_assignment(db=db, flight_assignment=flight_assignment)

@router.get("/flight_assignments/", response_model=List[schemas_flight_assignment.FlightAssignment])
def read_flight_assignments(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    flight_assignments = crud_flight_assignment.get_flight_assignments(db, skip=skip, limit=limit)
    return flight_assignments

@router.get("/flight_assignments/{assignment_id}", response_model=schemas_flight_assignment.FlightAssignment)
def read_flight_assignment(assignment_id: int, db: Session = Depends(get_db)):
    db_flight_assignment = crud_flight_assignment.get_flight_assignment(db, assignment_id=assignment_id)
    if db_flight_assignment is None:
        raise HTTPException(status_code=404, detail="FlightAssignment not found")
    return db_flight_assignment
