# app/services/auth_service.py

from app.core.security import create_access_token, hash_password, verify_password
from app.db.base import create_document, get_by_field

COLLECTION = "users"


async def register_user(data: dict):
    existing = await get_by_field(COLLECTION, "email", data["email"])
    if existing:
        return None

    data["password"] = hash_password(data["password"])
    return await create_document(COLLECTION, data)


async def login_user(email: str, password: str):
    user = await get_by_field(COLLECTION, "email", email)
    if not user:
        return None

    if not verify_password(password, user["password"]):
        return None

    token = create_access_token({"sub": user["_id"]})
    return token
