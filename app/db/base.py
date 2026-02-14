# app/db/base.py

from bson import ObjectId

from app.db.mongodb import get_collection


def serialize(doc):
    doc["_id"] = str(doc["_id"])
    return doc


async def create_document(collection: str, data: dict):
    col = get_collection(collection)
    result = await col.insert_one(data)
    return str(result.inserted_id)


async def get_document(collection: str, id: str):
    col = get_collection(collection)
    doc = await col.find_one({"_id": ObjectId(id)})
    return serialize(doc) if doc else None


async def get_by_field(collection: str, field: str, value):
    col = get_collection(collection)
    doc = await col.find_one({field: value})
    return serialize(doc) if doc else None


async def update_document(collection: str, id: str, data: dict):
    col = get_collection(collection)
    result = await col.update_one({"_id": ObjectId(id)}, {"$set": data})
    return result.modified_count


async def delete_document(collection: str, id: str):
    col = get_collection(collection)
    result = await col.delete_one({"_id": ObjectId(id)})
    return result.deleted_count


async def get_all_documents(collection: str):
    col = get_collection(collection)
    cursor = col.find()
    documents = []

    async for doc in cursor:
        documents.append(serialize(doc))

    return documents
