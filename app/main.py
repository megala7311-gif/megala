from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from .database import init_db
from app.routes import router


app = FastAPI(
    title="FitBuddy - AI Fitness Plan Generator",
    description="AI-powered powered personalized fitness plan generator using Gemini.",
    version="1.0.0",
)


#Serve CSS/static files
app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)


#Register application routes
app.include_router(router)


@app.on_event("startup")
def startup_event():
    """
    create database tables when the application starts.
    """
    init_db()