from fastapi import FastAPI

from app.api.auth_route import router as auth_router
from app.api.health_route import router as health_router
from app.api.user_route import router as user_router

app = FastAPI()

app.include_router(user_router)
app.include_router(auth_router)
app.include_router(health_router)
