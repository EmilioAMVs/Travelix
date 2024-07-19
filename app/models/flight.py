from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from infrastructure.databases.connection import Base

class Flight(Base):
    __tablename__ = 'flights'

    id = Column(Integer, primary_key=True, index=True)
    flight_number = Column(String(50), unique=True, index=True)
    departure_date = Column(DateTime)
    destination = Column(String(100))

    # Relación con los vuelos asignados
    user_flights = relationship('UserFlight', back_populates='flight')
