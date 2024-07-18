from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from infrastructure.databases.connection import Base


class Flight(Base):
    __tablename__ = 'flights'

    id = Column(Integer, primary_key=True, index=True)
    departure_city = Column(String)
    destination_city = Column(String)
    departure_time = Column(DateTime)
    arrival_time = Column(DateTime)
    passenger_id = Column(Integer, ForeignKey('users.id'))

    # Relación con el usuario que reservó el vuelo
    passenger = relationship("User", back_populates="flights")
