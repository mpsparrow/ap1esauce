from twitchio.ext import commands
from settings import PASS, CLIENTID, IDENT, PREFIX, CHANNEL

def write(filename: str, msg: str):
    log = open(f'{filename}','a+')
    log.write(f"{msg}\n")
    log.close()

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(irc_token=PASS, client_id=CLIENTID, nick=IDENT, prefix=PREFIX, initial_channels=CHANNEL)

    # Events don't need decorators when subclassed
    async def event_ready(self):
        print(f'Ready | {self.nick}')

    async def event_message(self, message):
        if isinstance(error, commands.CommandNotFound):
            await self.handle_commands(message)
        else:
            write(f"{message.channel}.txt", message.content)
            await self.handle_commands(message)

bot = Bot()
bot.run()