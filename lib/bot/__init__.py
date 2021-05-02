from datetime import datetime

from discord import Intents, colour
from discord.ext.commands import Bot as BotBase
from discord import Embed, File

from apscheduler.schedulers.asyncio import AsyncIOScheduler

PREFIX = "!p"
OWNER_IDS = [515161252037787659]

class Bot(BotBase):
    def __init__(self):
        
        self.PREFIX = PREFIX
        self.ready = False
        self.guild = None
        self.scheduler = AsyncIOScheduler()
        
        super().__init__(
            command_prefix=PREFIX, 
            owner_ids=OWNER_IDS,
            intends=Intents.all()
            )
        
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
            
            channel = self.get_channel(823477241324371968)
            
            embed = Embed(
                title="Now online!", 
                description="PitrBot is now online.", 
                colour=0xFF0000,
                timestamp=datetime.utcnow()
                )
            fields = [
                ("Name", "Value", True),
                ("Another field", "This field is next to the other one", True),
                ("A non-inline field", "This field will appear on it's own row.", False)
                ]
            for name, value, inline, in fields:
                embed.add_field(name=name, value=value, inline=inline)
            embed.set_author(name="PitrBot Dev", icon_url=self.guild.icon_url)
            embed.set_footer(text="This is a footer")
            embed.set_thumbnail(url=self.guild.icon_url)
            embed.set_image(url=self.guild.icon_url)
            await channel.send(embed=embed)
            
            await channel.send(file=File("./data/images/pick.jpg"))
            
        else:
            print("bot reconnected")
    
    async def on_message(self):
        pass
    
bot = Bot()