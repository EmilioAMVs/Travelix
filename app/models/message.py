from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from APIs.db.connection import Base

class Message(Base):
    __tablename__ = 'messages'

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String(250))
    user_id = Column(Integer, ForeignKey('users.id'))

    # Relaciones
    user = relationship('User')
