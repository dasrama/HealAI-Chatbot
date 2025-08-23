import os
from bot.commands import bot   # assuming your bot code is in app/bot.py
from config.settings import Settings

if __name__ == "__main__":
    # Get Discord token from env (recommended)
    TOKEN = Settings().DISCORD_BOT_TOKEN

    if not TOKEN:
        raise ValueError("⚠️ Discord bot token not found. Please set DISCORD_BOT_TOKEN env var.")

    bot.run(TOKEN)
