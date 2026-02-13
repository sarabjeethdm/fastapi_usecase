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
def create(user: UserCreate):
    user_id = create_user(user.dict())
    return {"id": user_id}


@router.get("/{user_id}")
def read(user_id: str):
    user = get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.get("/")
def read_all():
    return get_users()


@router.put("/{user_id}")
def update(user_id: str, user: UserCreate):
    updated = update_user(user_id, user.dict())
    if not updated:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User updated"}


@router.delete("/{user_id}")
def delete(user_id: str):
    deleted = delete_user(user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted"}
