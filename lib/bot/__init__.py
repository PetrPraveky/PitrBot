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
        
    def run(self, version):
        self.version = version
        
        with open("./lib/bot/token.0", "r", encoding="utf-8") as tf:
            self.TOKEN = tf.read()
            
        print("running bot..")
        super().run(self.TOKEN, reconnect=True)
    
    async def on_connect(self):
        print("bot connected")
        
    async def on_disconnect(self):
        print("bot disconnected")
        
    async def on_ready(self):
        if not self.ready:
            self.ready = True
            self.guild = self.get_guild(818123510366732328)
            print("bot ready")
        else:
            print("bot reconnected")
    
    async def on_message(self):
        pass
    
bot = Bot()