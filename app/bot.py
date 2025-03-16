import discord
from discord.ext import commands
from app.service.ai_engine import get_medical_response
from config import config 


DISCORD_BOT_TOKEN = config.get("DISCORD_BOT_TOKEN") 

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
    await ctx.send(f"hello {ctx.author} !!")    


@bot.command()
async def ask(ctx, *, question):
    response = get_medical_response(question=question, max_tokens=100)
    await ctx.send(response)

@bot.command()
async def symptoms(ctx, *, symptom):
    query = f"What are the possible causes of {symptom}?"
    response = get_medical_response(query, max_tokens=70)
    await ctx.send(response)

@bot.command()
async def disease(ctx, *, disease_name):
    query = f"Give me detailed information about {disease_name}."
    response = get_medical_response(query, max_tokens=200)
    await ctx.send(response)

@bot.command()
async def firstaid(ctx, *, condition):
    query = f"What are the first aid steps for {condition}?"
    response = get_medical_response(query, max_tokens=100)
    await ctx.send(response["message"]["content"])

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

bot.run(token=DISCORD_BOT_TOKEN)   