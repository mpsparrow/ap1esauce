import os
from twitchio.ext import commands
from settings import PASS, CLIENTID, IDENT, PREFIX, CHANNEL

# set up the bot
bot = commands.Bot(
    irc_token=PASS,
    client_id=CLIENTID,
    nick=IDENT,
    prefix=PREFIX,
    initial_channels=CHANNEL
)

@bot.event
async def event_ready():
    'Called once when the bot goes online.'
    print(f"{IDENT} is online!")
    ws = bot._ws  # this is only needed to send messages within event_ready
    await ws.send_privmsg(CHANNEL, f"/me has landed!")


@bot.event
async def event_message(ctx):
    'Runs every time a message is sent in chat.'
    print("run")
    print(ctx.content)
    
    # make sure the bot ignores itself and the streamer
    if ctx.author.name.lower() == IDENT.lower():
        return

    await bot.handle_commands(ctx)

    # await ctx.channel.send(ctx.content)

    if 'hello' in ctx.content.lower():
        await ctx.channel.send(f"Hi, @{ctx.author.name}!")


@bot.command(name='test')
async def test(ctx):
    await ctx.send('test passed!')


if __name__ == "__main__":
    bot.run()