# app/api/user_route.py

from fastapi import APIRouter, HTTPException
from app.models.user_model import UserCreate
from app.services.user_service import (
    create_user,
    delete_user,
    get_user,
    get_users,
    update_user,
)

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/")
async def create(user: UserCreate):
    user_id = await create_user(user.dict())
    return {"id": user_id}


@router.get("/{user_id}")
async def read(user_id: str):
    user = await get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.get("/")
async def read_all():
    return await get_users()


@router.put("/{user_id}")
async def update(user_id: str, user: UserCreate):
    updated = await update_user(user_id, user.dict())
    if not updated:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User updated"}


@router.delete("/{user_id}")
async def delete(user_id: str):
    deleted = await delete_user(user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted"}

