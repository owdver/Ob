from pyrogram import filters
from bot import bot
from utils.api_helpers import spell_check, shorten_url

@bot.on_message(filters.command("shorten") & filters.private)
async def shorten(client, message):
    url = message.text.split(maxsplit=1)[1]
    short_url = shorten_url(url)
    await message.reply(short_url)

@bot.on_message(filters.command("stream") & filters.private)
async def stream_video(client, message):
    file_id = message.text.split(maxsplit=1)[1]
    # Logic to generate stream URL
    stream_url = f"http://example.com/stream/{file_id}"
    await message.reply(stream_url)

@bot.on_message(filters.text)
async def check_spelling(client, message):
    corrected_text = spell_check(message.text)
    if corrected_text != message.text:
        await message.reply(f"Did you mean: {corrected_text}")