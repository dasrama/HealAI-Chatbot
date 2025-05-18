from fastapi import FastAPI
from app.bot.bot import bot
from app.config.settings import Settings
from contextlib import asynccontextmanager
import asyncio

@asynccontextmanager
async def lifespan(app: FastAPI):
    bot_task = asyncio.create_task(bot.start(Settings().DISCORD_BOT_TOKEN))
    yield
    # Cleanup when shutting down
    await bot.close()
    await bot_task

app = FastAPI(lifespan=lifespan)
