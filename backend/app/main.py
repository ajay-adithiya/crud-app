from fastapi import FastAPI

from .database import engine
from .models import Base
from .routers.user import router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="User Registration API"
)

app.include_router(router)

@app.get("/")
def home():
    return {
        "message": "API Running"
    }