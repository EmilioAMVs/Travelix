# app/models/__init__.py
from app.APIs.db.connection import Base
from app.models.activity import Activity
from app.models.flight_assignment import FlightAssignment
from app.models.flight import Flight
from app.models.user_flight import UserFlight
from app.models.user import User
from app.models.itinerary import Itinerary
from app.models.message import Message
