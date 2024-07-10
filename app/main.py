from fastapi import FastAPI
from app.APIs.routes import user_routes, itinerary_routes, activity_routes, flight_routes, message_routes

app = FastAPI()

# Incluye tus rutas
app.include_router(user_routes, prefix="/users", tags=["Users"])
app.include_router(itinerary_routes, prefix="/itineraries", tags=["Itineraries"])
app.include_router(activity_routes, prefix="/activities", tags=["Activities"])
app.include_router(flight_routes, prefix="/flights", tags=["Flights"])
app.include_router(message_routes, prefix="/messages", tags=["Messages"])

@app.get("/")
def read_root():
    return {"Welcome to the Travel Platform API"}
