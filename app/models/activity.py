from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from APIs.db.connection import Base

class Activity(Base):
    __tablename__ = 'activities'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True)
    description = Column(String(250))
    itinerary_id = Column(Integer, ForeignKey('itineraries.id'))

    # Relaciones
    itinerary = relationship('Itinerary', back_populates='activities')
