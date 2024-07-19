from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from infrastructure.databases.connection import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, index=True) 
    hashed_password = Column(String)

    # Relación con los vuelos de los usuarios
    flights = relationship('UserFlight', back_populates='user')
