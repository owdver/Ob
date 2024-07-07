import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
DATABASE_URI = os.getenv("DATABASE_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME")
ADMINS = os.getenv("ADMINS").split()  # List of admin user IDs or usernames
CHANNELS = os.getenv("CHANNELS").split()  # List of channel IDs or usernames

# Debugging: Print ADMINS
print(f"ADMINS: {ADMINS}")
