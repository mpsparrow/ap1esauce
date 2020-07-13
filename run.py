from twitchio.ext import commands
from settings import PASS, CLIENTID, CLIENTSECRET, IDENT, PREFIX, CHANNEL

def write(filename: str, msg: str):
    log = open(f'{filename}','a+')
    log.write(f"{msg}\n")
    log.close()

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(irc_token=PASS, client_id=CLIENTID, client_secret=CLIENTSECRET, nick=IDENT, prefix=PREFIX, initial_channels=CHANNEL)

    # Events don't need decorators when subclassed
    async def event_ready(self):
        print(f'Ready | {self.nick}')

    async def event_command_error(self, error: Exception, data=None):
        if isinstance(error, commands.CommandNotFound):
            return

    async def event_message(self, message):
        try:
            data = await self.get_stream(message.channel)
            print("-1")
            print(data)
            if data is not None:
                print("0")
                write(f"{message.channel}.txt", message.content)
                await self.handle_commands(message)
            else:
                print("1")
        except Exception as e:
            print(e)

bot = Bot()
bot.run()