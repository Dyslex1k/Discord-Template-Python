from discord.ext import commands

class ReadyListener(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Ready! Logged in as {self.bot.user}")

async def setup(bot: commands.Bot):
    await bot.add_cog(ReadyListener(bot))