from fastapi import APIRouter

from app.api.routes import shortlink

api_router = APIRouter()
api_router.include_router(shortlink.router, prefix="/shortlinks", tags=["shortlinks"])
