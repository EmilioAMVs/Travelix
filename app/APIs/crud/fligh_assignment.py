from sqlalchemy.orm import Session
from models.flight_assignment import FlightAssignment
from schemas.flight_assignment import FlightAssignmentCreate

def get_flight_assignment(db: Session, assignment_id: int):
    return db.query(FlightAssignment).filter(FlightAssignment.id == assignment_id).first()

def get_flight_assignments(db: Session, skip: int = 0, limit: int = 10):
    return db.query(FlightAssignment).offset(skip).limit(limit).all()

def create_flight_assignment(db: Session, flight_assignment: FlightAssignmentCreate):
    db_flight_assignment = FlightAssignment(
        flight_id=flight_assignment.flight_id,
        assigned_user_id=flight_assignment.assigned_user_id
    )
    db.add(db_flight_assignment)
    db.commit()
    db.refresh(db_flight_assignment)
    return db_flight_assignment
