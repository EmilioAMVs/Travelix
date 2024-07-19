from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.APIs.db.connection import Base

class Itinerary(Base):
    __tablename__ = 'itineraries'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), index=True)
    description = Column(String(250))

    # Relaciones
    activities = relationship('Activity', back_populates='itinerary')
