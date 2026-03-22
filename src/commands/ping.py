import discord
from discord import app_commands
from discord.ext import commands

class Ping(commands.Cog):
    # Annotating bot as commands.Bot or commands.GroupCog
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="ping", description="Replies with Pong!")
    async def ping(self, interaction: discord.Interaction):
        await interaction.response.send_message("Pong!")

# Annotating the bot parameter here fixes the 'setup' errors
async def setup(bot: commands.Bot):
    await bot.add_cog(Ping(bot))