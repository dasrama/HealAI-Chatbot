from app.bot.bot import bot
from app.config.setting import Settings


if __name__=="__main__":
    bot.run(Settings().DISCORD_BOT_TOKEN)