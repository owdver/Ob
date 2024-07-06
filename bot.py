import logging
from pyrogram import Client
from config import BOT_TOKEN, API_ID, API_HASH

# Enable logging
logging.basicConfig(level=logging.INFO)

# Initialize bot
bot = Client("my_bot", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH)

# Import handlers
from handlers import commands, features

# Run the bot
if __name__ == "__main__":
    bot.run()