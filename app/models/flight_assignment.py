from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from infrastructure.databases.connection import Base

class FlightAssignment(Base):
    __tablename__ = 'flight_assignments'

    id = Column(Integer, primary_key=True, index=True)
    flight_id = Column(Integer, ForeignKey('flights.id'))
    assigned_user_id = Column(Integer, ForeignKey('users.id'))

    # Relaciones
    flight = relationship('Flight', back_populates='assignments')
    assigned_user = relationship('User', back_populates='assignments') 
