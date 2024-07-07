import logging
import signal
import sys
from pyrogram import Client
from config import BOT_TOKEN, API_ID, API_HASH

# Enable logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize bot
bot = Client("my_bot", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH)

# Import handlers
from handlers import commands, features

# Log handler registration
logger.info("Command handlers and features imported successfully.")

# Signal handler to log SIGTERM and SIGINT
def signal_handler(sig, frame):
    logger.info(f"Stop signal received ({signal.Signals(sig).name}). Exiting...")
    bot.stop()
    sys.exit(0)

signal.signal(signal.SIGTERM, signal_handler)
signal.signal(signal.SIGINT, signal_handler)

# Run the bot
if __name__ == "__main__":
    logger.info("Starting the bot...")
    bot.run()
