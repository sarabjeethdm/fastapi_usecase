from pymongo import MongoClient
from app.core.config import settings 

client = MongoClient(settings.MONGO_URI)

database = client[settings.DB_NAME]

def get_collection(collection_name: str):
    return database[collection_name]
