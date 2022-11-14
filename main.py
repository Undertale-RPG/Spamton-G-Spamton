import os
import disnake
from disnake import AllowedMentions
from dotenv import load_dotenv
from disnake.ext import commands
from motor.motor_asyncio import AsyncIOMotorClient

load_dotenv()

intents = disnake.Intents(messages=True, guilds=True)

class SpamtonBot(commands.AutoShardedInteractionBot):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.BotToken = os.getenv("TOKEN")
        self.activity = disnake.Game("Together with all of you")
        self.help_command = None
        self.error_webhook = os.getenv("ERROR_WEBHOOK")

    def load_all_cogs(self):
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py") and not filename.startswith("_"):
                self.load_extension(f"cogs.{filename[:-3]}")
                print(f"🔁 cogs.{filename[:-3]} is loaded and ready.")
        return


bot = SpamtonBot(
    intents=intents,
    owner_ids=[536538183555481601, 1023550762816638996],
    allowed_mentions=AllowedMentions(
        users=True,
        everyone=False,
        roles=True,
        replied_user=True,
    )
)


bot.load_all_cogs()
bot.run(bot.BotToken)