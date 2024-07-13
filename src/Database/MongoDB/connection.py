from pymongo import MongoClient
from dotenv import load_dotenv
from loguru import logger
import os

load_dotenv()

logger.add("database.log", rotation="500 MB")

DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = int(os.getenv('DB_PORT', 27017))
DB_NAME = os.getenv('DB_NAME', 'databaseMicro')

client = MongoClient(DB_HOST, DB_PORT)
db = client[DB_NAME]
reports_collection = db.reports
resource_collection= db.resources
downloadable_collection= db.downloadables


try:
    client = MongoClient(DB_HOST, DB_PORT)
    db = client[DB_NAME]
    reports_collection = db.reports
    resource_collection = db.resources
    downloadable_collection = db.downloadables
    logger.info("Connected to MongoDB successfully")
except Exception as e:
    logger.error(f"Failed to connect to MongoDB: {e}")
