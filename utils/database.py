from motor.motor_asyncio import AsyncIOMotorClient
from config import DATABASE_URI, DATABASE_NAME
import logging

logger = logging.getLogger(__name__)

try:
    client = AsyncIOMotorClient(DATABASE_URI)
    db = client[DATABASE_NAME]
    logger.info("Connected to the database successfully.")
except Exception as e:
    logger.error(f"Failed to connect to the database: {e}")
