import discord
from discord.ext import commands
from discord.ext.commands import Context

from service.ai_engine import get_medical_response

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")


@bot.command()
async def hello(ctx: Context):
    await ctx.send(f"hello {ctx.author.display_name} !!")    


@bot.command()
async def ask(ctx: Context, *, question):
    response = get_medical_response(question)
    await ctx.send(response)


@bot.command()
async def symptoms(ctx: Context, *, symptom):
    question = f"What are the possible causes of {symptom}?"
    response = get_medical_response(question)
    await ctx.send(response)


@bot.command()
async def disease(ctx: Context, *, disease_name):
    question = f"Give me detailed information about {disease_name}."
    response = get_medical_response(question)
    await ctx.send(response)


@bot.command()
async def firstaid(ctx: Context, *, condition):
    question = f"What are the first aid steps for {condition}?"
    response = get_medical_response(question)
    await ctx.send(response)


@bot.command()
async def info(ctx: Context):
    info_text = (
        "**Available Commands:**\n"
        "!ask [question] - Ask a medical question\n"
        "!symptoms [symptom] - Get possible causes\n"
        "!disease [disease_name] - Learn about diseases\n"
        "!firstaid [condition] - Get first aid tips\n"
        "!info - Show this message"
    )
    await ctx.send(info_text)
