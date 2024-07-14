from fastapi import APIRouter
from app.APIs.routes import user_routes, itinerary_routes, activity_routes, flight_routes, message_routes

router = APIRouter()

router.include_router(user_routes, prefix="/users", tags=["Users"])
router.include_router(itinerary_routes, prefix="/itineraries", tags=["Itineraries"])
router.include_router(activity_routes, prefix="/activities", tags=["Activities"])
router.include_router(flight_routes, prefix="/flights", tags=["Flights"])
router.include_router(message_routes, prefix="/messages", tags=["Messages"])
