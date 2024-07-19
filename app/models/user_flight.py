from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from infrastructure.databases.connection import Base

class UserFlight(Base):
    __tablename__ = 'user_flights'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    flight_id = Column(Integer, ForeignKey('flights.id'))

    # Relaciones
    user = relationship('User', back_populates='flights')
    flight = relationship('Flight', back_populates='user_flights')
