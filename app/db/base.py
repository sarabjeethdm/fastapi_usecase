from bson import ObjectId

from app.db.mongodb import get_collection


def serialize_doc(doc):
    doc["_id"] = str(doc["_id"])
    return doc


def create_document(collection_name: str, data: dict):
    collection = get_collection(collection_name)
    result = collection.insert_one(data)
    return str(result.inserted_id)


def get_document(collection_name: str, document_id: str):
    collection = get_collection(collection_name)
    doc = collection.find_one({"_id": ObjectId(document_id)})
    if doc:
        return serialize_doc(doc)
    return None


def get_all_documents(collection_name: str):
    collection = get_collection(collection_name)
    docs = collection.find()
    return [serialize_doc(doc) for doc in docs]


def update_document(collection_name: str, document_id: str, data: dict):
    collection = get_collection(collection_name)
    result = collection.update_one({"_id": ObjectId(document_id)}, {"$set": data})
    return result.modified_count


def delete_document(collection_name: str, document_id: str):
    collection = get_collection(collection_name)
    result = collection.delete_one({"_id": ObjectId(document_id)})
    return result.deleted_count
