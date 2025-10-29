import os
from bot.commands import bot   
from config.settings import Settings

if __name__ == "__main__":
    TOKEN = Settings().DISCORD_BOT_TOKEN

    if not TOKEN:
        raise ValueError("⚠️ Discord bot token not found. Please set DISCORD_BOT_TOKEN env var.")

    bot.run(TOKEN)
