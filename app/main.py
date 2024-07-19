from fastapi import FastAPI
from app.APIs.routes.user_routes import router as user_routes
from app.APIs.routes.itinerary_routes import router as itinerary_routes
from app.APIs.routes.activity_routes import router as activity_routes
from app.APIs.routes.flight_routes import router as flight_routes
from app.APIs.routes.message_routes import router as message_routes

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
