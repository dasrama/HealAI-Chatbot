import discord
import asyncio
from discord import Embed
from discord.ext import commands
from discord.ext.commands import Context

from service.ai_engine import get_medical_response
from utils.sanitise import contains_markdown_code

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
    if contains_markdown_code(question):
        await ctx.send("Please do not include markdown or code blocks in your input.")
        return
    try:
        async with ctx.typing():    
            response = await asyncio.to_thread(get_medical_response, question)
        await ctx.send(response)
    except Exception as e:
        await ctx.send("Sorry, something went wrong while processing your request.")


@bot.command()
async def symptoms(ctx: Context, *, symptom):
    if contains_markdown_code(symptom):
        await ctx.send("Please do not include markdown or code blocks in your input.")
        return
    try:  
        async with ctx.typing():  
            question = f"What are the possible causes of {symptom}?"
            response = await asyncio.to_thread(get_medical_response, question)
        await ctx.send(response)
    except Exception as e:
        await ctx.send("Sorry, something went wrong while processing your request")
        print(str(e))


@bot.command()
async def disease(ctx: Context, *, disease_name):
    if contains_markdown_code(disease_name):
        await ctx.send("Please do not include markdown or code blocks in your input.")
        return
    try:
        async with ctx.typing():  
            question = f"Give me detailed information about {disease_name}."
            response = await asyncio.to_thread(get_medical_response, question)
        await ctx.send(response)
    except Exception as e:
        await ctx.send("Sorry, something went wrong while processing your request")


@bot.command()
async def firstaid(ctx: Context, *, condition):
    if contains_markdown_code(condition):
        await ctx.send("Please do not include markdown or code blocks in your input.")
        return
    try:
        async with ctx.typing():  
            question = f"What are the first aid steps for {condition}?"
            response = await asyncio.to_thread(get_medical_response, question)
        await ctx.send(response)
    except Exception as e:
        await ctx.send("Sorry, something went wrong while processing your request")    


@bot.command()
async def info(ctx: Context):
    embed = Embed(title="Available Commands", color=0x1abc9c)
    embed.add_field(name="!ask [question]", value="Ask a medical question", inline=False)
    embed.add_field(name="!symptoms [symptom]", value="Get possible causes", inline=False)
    embed.add_field(name="!disease [disease_name]", value="Learn about diseases", inline=False)
    embed.add_field(name="!firstaid [condition]", value="Get first aid tips", inline=False)
    embed.add_field(name="!info", value="Show this message", inline=False)

    await ctx.send(embed=embed)
