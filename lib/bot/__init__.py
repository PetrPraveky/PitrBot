from discord.ext.commands import Bot as BotBase
from apscheduler.schedulers.asyncio import AsyncIOScheduler

PREFIX = "!p"
OWNER_IDS = [515161252037787659]

class Bot(BotBase):
    def __init__(self):
        
        self.PREFIX = PREFIX
        self.ready = False
        self.guild = None
        self.scheduler = AsyncIOScheduler()
        
        super().__init__(command_prefix=PREFIX, owner_ids=OWNER_IDS)
        
    def run(self):
        pass
    
    async def on_connect(self):
        print("bot connected")
        
    async def on_disconnect(self):
        print("bot disconnected")
        
    async def on_ready(self):
        pass
    
    async def on_message(self):
        pass
    
bot = Bot()