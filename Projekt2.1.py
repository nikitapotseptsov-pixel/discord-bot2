import discord
from discord.ext import commands
from datetime import datetime

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Bot töötab")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    pahad_sonad = ["loll", "idiot"]
    tekst = message.content.lower()
    
    for sona in pahad_sonad:
        if sona in tekst:
            await message.delete()
            await message.channel.send("Ära ropenda!")
            return
    await bot.process_commands(message)

@bot.command()
async def ping(ctx):
    await ctx.send("Pong")

@bot.command()
async def delete(ctx, mitu):
    mitu = int(mitu)
    await ctx.channel.purge(limit=mitu + 1)
    await ctx.send(f"Kustutasin {mitu} sõnumit!")

@bot.command()
async def time(ctx):
    kell = datetime.now().strftime("%H:%M")
    await ctx.send(f"Kell on praegu {kell}")

bot.run("MTUwMDgxNjc1NjA2OTg5NjI3Mw.GupHWL.zZS5jSe0237YrYLYCNA-RO2rQvxuF5lzdUvITY")