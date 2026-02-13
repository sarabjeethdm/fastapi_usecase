from fastapi import FastAPI

from app.api.user_route import router as user_router

app = FastAPI()

app.include_router(user_router)
