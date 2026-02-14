# app/api/auth_route.py

from fastapi import APIRouter, HTTPException, Response

from app.models.auth_model import LoginModel, RegisterModel
from app.services.auth_service import login_user, register_user

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register")
async def register(data: RegisterModel):
    user = await register_user(data.dict())
    if not user:
        raise HTTPException(status_code=400, detail="Email already exists")
    return {"message": "User created"}


@router.post("/login")
async def login(data: LoginModel, response: Response):
    token = await login_user(data.email, data.password)
    if not token:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    response.set_cookie(
        key="access_token",
        value=token,
        httponly=True,  # prevents JS access
        samesite="lax",  # adjust for frontend
    )
    return {"message": "Logged in"}
