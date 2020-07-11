from twitchio.ext import commands
from settings import PASS, CLIENTID, IDENT, PREFIX, CHANNEL

class Bot(commands.Bot):

    def __init__(self):
        super().__init__(irc_token=PASS, client_id=CLIENTID, nick=IDENT, prefix=PREFIX,
                         initial_channels=CHANNEL)

    # Events don't need decorators when subclassed
    async def event_ready(self):
        print(f'Ready | {self.nick}')

    async def event_message(self, message):
        print(f"{message.channel} | {message.author.name}: {message.content}")
        await self.handle_commands(message)

    # Commands use a different decorator
    @commands.command(name='testing')
    async def my_command(self, ctx):
        await ctx.send(f'Hello {ctx.author.name}!')

bot = Bot()
bot.run()