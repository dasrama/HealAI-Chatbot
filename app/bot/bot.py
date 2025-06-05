import httpx
import discord
from discord.ext import commands
from discord.ext.commands import Context
from app.service.ai_engine import get_medical_response
from app.service.memory import get_user_session, store_chat
from app.config.settings import Settings 
from app.backend.models.chat import ChatPayload

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command
async def message(ctx):
    await ctx.send(f"hello {ctx.author} !!!")

@bot.command()
async def hello(ctx):
    print(ctx.author)
    await ctx.send(f"hello {ctx.author} !!")    

@bot.command()
async def ask(ctx: Context, *, question):
    payload = ChatPayload(
        user_id=ctx.author.id,
        question=question
    )
    async with httpx.AsyncClient() as client:
        x = client.post("f{URL}/ask", json=payload.model_dump())
        response = x.json()
    await ctx.send(response["answer"])

@bot.command()
async def symptoms(ctx: Context, *, symptom):
    question = f"What are the possible causes of {symptom}?"
    payload = ChatPayload(
        user_id=ctx.author.id,
        question=question
    )
    async with httpx.AsyncClient() as client:
        x = client.post("f{URL}/symptoms", json=payload.model_dump())
        response = x.json()
    await ctx.send(response["answer"])

@bot.command()
async def disease(ctx: Context, *, disease_name):
    question = f"Give me detailed information about {disease_name}."
    payload = ChatPayload(
        user_id=ctx.author.id,
        question=question
    )
    async with httpx.AsyncClient() as client:
        x = client.post("f{URL}/symptoms", json=payload.model_dump())
        response = x.json()
    await ctx.send(response["answer"])

@bot.command()
async def firstaid(ctx: Context, *, condition):
    question = f"What are the first aid steps for {condition}?"
    payload = ChatPayload(
        user_id=ctx.author.id,
        question=question
    )
    async with httpx.AsyncClient() as client:
        x = client.post("f{URL}/symptoms", json=payload.model_dump())
        response = x.json()
    await ctx.send(response["answer"])

@bot.command()
async def info(ctx):
    info_text = (
        "**Available Commands:**\n"
        "/ask [question] - Ask a medical question\n"
        "/symptoms [symptom] - Get possible causes\n"
        "/disease [disease_name] - Learn about diseases\n"
        "/firstaid [condition] - Get first aid tips\n"
        "/history - View previous interactions\n"
        "/clearhistory - Delete stored chat history\n"
        "/help - Show this message"
    )
    await ctx.send(info_text)
