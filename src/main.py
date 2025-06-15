import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot connected as {bot.user}")
    await bot.change_presence(activity=discord.Game(name="Loading Spotify..."))

bot.run(os.getenv("DISCORD_TOKEN"))
