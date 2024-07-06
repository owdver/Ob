from pyrogram import filters
from bot import bot
from utils.database import db

@bot.on_message(filters.command("index") & filters.user(db.ADMINS))
async def index_files(client, message):
    await message.reply("Indexing files...")
    # Logic to index files from your channel
    await message.reply("Indexing completed.")

@bot.on_message(filters.command("logs") & filters.user(db.ADMINS))
async def get_logs(client, message):
    logs = "Recent Errors: ..."  # Fetch logs
    await message.reply(logs)

@bot.on_message(filters.command("userinfo") & filters.private)
async def user_info(client, message):
    user_id = message.from_user.id
    user_data = await db.users.find_one({"user_id": user_id})
    await message.reply(str(user_data))

@bot.on_message(filters.command("start") & filters.private)
async def start(client, message):
    await message.reply("Hello! I am your bot. Use /help to see available commands.")

@bot.on_message(filters.command("help") & filters.private)
async def help(client, message):
    help_text = """
    Available Commands:
    /index - index file from your channel
    /logs - to get the recent errors
    /userinfo - get user info
    /start - start the bot
    /help - show this help message
    """
    await message.reply(help_text)