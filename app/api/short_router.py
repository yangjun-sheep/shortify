from fastapi import APIRouter

from app.api.routes import redirect

api_router = APIRouter()
api_router.include_router(redirect.router, prefix="/t", tags=["redirect"])
