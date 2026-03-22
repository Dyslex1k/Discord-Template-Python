import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

class MyBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        # Ensure message_content is enabled if you need prefix commands, 
        # otherwise, Guilds is enough for Slash Commands.
        super().__init__(command_prefix="!", intents=intents)

    async def setup_hook(self):
        # List of folders to scan for autoloading
        folders = ["commands", "Listeners"]
        
        for folder in folders:
            if not os.path.exists(folder):
                continue
                
            for filename in os.listdir(folder):
                if filename.endswith(".py") and not filename.startswith("__"):
                    # Converts 'commands/ping.py' to 'commands.ping'
                    extension = f"{folder}.{filename[:-3]}"
                    try:
                        await self.load_extension(extension)
                        print(f"Loaded {extension}")
                    except Exception as e:
                        print(f"Failed to load {extension}: {e}")

        # This replaces deploy-commands.ts by syncing on start
        await self.tree.sync()

bot = MyBot()

if __name__ == "__main__":
    bot.run(str(os.getenv("DISCORD_TOKEN")))