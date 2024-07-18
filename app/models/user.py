from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from infrastructure.databases.connection import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    
        # Relación con los vuelos reservados por el usuario
    flights = relationship("Flight", back_populates="passenger")
