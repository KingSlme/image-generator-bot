import discord
from discord import app_commands
from discord.ext import commands
from image_generator import get_random_image

def run_discord_bot(TOKEN):
    bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

    @bot.event
    async def on_ready():
        print(f"{bot.user} is now running!")
        try:
            synced = await bot.tree.sync()
            print(f"Synced {len(synced)} command(s)")
        except Exception as e:
            print(e)

    @bot.tree.command(name="image")
    @app_commands.describe(image= "The image to generate")
    async def say(interaction: discord.Interaction, image: str):
        # Ensures bot cannot be used in private messages
        if interaction.guild:
            await interaction.response.send_message(f"{get_random_image({image})}")

    bot.run(TOKEN)