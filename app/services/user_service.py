# app/services/user_service.py

from app.db.base import (
    create_document,
    delete_document,
    get_all_documents,
    get_document,
    update_document,
)

COLLECTION_NAME = "users"


def create_user(data: dict):
    return create_document(COLLECTION_NAME, data)


def get_user(user_id: str):
    return get_document(COLLECTION_NAME, user_id)


def get_users():
    return get_all_documents(COLLECTION_NAME)


def update_user(user_id: str, data: dict):
    return update_document(COLLECTION_NAME, user_id, data)


def delete_user(user_id: str):
    return delete_document(COLLECTION_NAME, user_id)
