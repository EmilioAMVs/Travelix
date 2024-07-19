from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

from app.APIs.routes import activity, flight, flight_assignment, user, user_flight, itinerary, message
from app.APIs.crud import activity, flight, flight_assignment, user, user_flight, itinerary, message

app = FastAPI()

# Configuración de CORS
origins = [
    "http://localhost",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Montar archivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configurar plantillas
templates = Jinja2Templates(directory="app/templates")

# Incluir rutas de APIs
app.include_router(activity.router, prefix="/activities", tags=["activities"])
app.include_router(flight.router, prefix="/flights", tags=["flights"])
app.include_router(flight_assignment.router, prefix="/flight-assignments", tags=["flight-assignments"])
app.include_router(user.router, prefix="/users", tags=["users"])
app.include_router(user_flight.router, prefix="/user-flights", tags=["user-flights"])
app.include_router(itinerary.router, prefix="/itineraries", tags=["itineraries"])
app.include_router(message.router, prefix="/messages", tags=["messages"])

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
