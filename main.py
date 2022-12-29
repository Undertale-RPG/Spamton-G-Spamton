import os
import disnake
from disnake import AllowedMentions
from dotenv import load_dotenv
from disnake.ext import commands
from utility.utils import ConsoleColors
from motor.motor_asyncio import AsyncIOMotorClient

load_dotenv()

intents = disnake.Intents.default()
intents.members = True
intents.message_content = True

class SpamtonBot(commands.AutoShardedInteractionBot):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.BotToken = os.getenv("TOKEN")
        self.activity = disnake.Game("Together with all of you")
        self.help_command = None
        self.error_webhook = os.getenv("ERROR_WEBHOOK")
        self.MongoUrl = os.getenv("MONGO_URL")
        self.cluster = AsyncIOMotorClient(self.MongoUrl)
        self.db = None
        self.guilds_db = None

    async def on_shard_connect(self, shard):
        print(
            f"{ConsoleColors.CYAN}---------- {ConsoleColors.GREEN}Shard {shard} is on {ConsoleColors.CYAN}-------------\n"
            f"{ConsoleColors.GREEN}Total Guilds: {len(self.guilds)}\n"
            f"{ConsoleColors.GREEN}Total Shards: {len(self.shards)}\n"
            f"{ConsoleColors.CYAN}--------------------------------------{ConsoleColors.ENDC}"
        )

    def load_all_cogs(self):
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py") and not filename.startswith("_"):
                self.load_extension(f"cogs.{filename[:-3]}")
                print(f"{ConsoleColors.GREEN}🔁 cogs.{filename[:-3]} is loaded and ready.")
        return

bot = SpamtonBot(
    intents=intents,
    owner_ids=[536538183555481601],
    allowed_mentions=AllowedMentions(
        users=True,
        everyone=False,
        roles=True,
        replied_user=True,
    )
)


bot.load_all_cogs()
bot.run(bot.BotToken)