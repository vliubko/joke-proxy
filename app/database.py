import logging
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from app.config import MONGO_URI, DB_NAME
from app.logging import setup_logging

# Setup logging
logger = setup_logging()

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db["jokes"]
    
def check_db_connection():
    try:
        logger.info(f"Connecting to MongoDB {DB_NAME} at {MONGO_URI}")
        result = db.command("ping")
        logger.info(f"Ping result: {result}")
        return result
    except Exception as e:
        logger.error(f"MongoDB connection error: {str(e)}")
        raise ConnectionFailure(f"Failed to connect to MongoDB: {str(e)}")

def save_joke(joke: str):
    collection.insert_one({"joke": joke})
