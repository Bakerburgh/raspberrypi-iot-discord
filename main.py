import cliargs
from config import Config
from discord.ext import commands
import iotpi
import os
import signal
import context
import asyncio
import sys

cli = cliargs.CliArgs()
config = Config(cli.config_filename)
bot = commands.Bot(command_prefix=config.discord_prefix, description=config.discord_description)
server = None
ctx = context.Context(bot)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    print("Server: {0}".format(config.discord_server))
    ctx.server = bot.get_server(config.discord_server)
    print('Server: ' + str(ctx.server))
    ctx.channel = ctx.server.get_channel(config.discord_channel)
    print('Reporting to channel: ' + str(ctx.channel))
    ipaddr = iotpi.get_ipaddr()
    print('Self IP address is ' + ipaddr)
    await bot.send_message(ctx.channel, "Hello World! I'm hailing from " + ipaddr)


@bot.command()
async def ip():
    """Get the IP address of this Raspberry Pi"""
    ipaddr = iotpi.get_ipaddr()
    await bot.say(ipaddr)


@bot.command()
async def shutdown():
    """Shut down this Raspberry Pi"""
    await bot.say("Goodbye")
    os.system("sudo shutdown -h now")


@bot.command()
async def reboot():
    """Reboot this Raspberry Pi"""
    await bot.say("I'll be back.")
    os.system("sudo reboot")


@bot.command()
async def signout():
    await bot.say("Farewell")
    await bot.close()


@bot.command()
async def add(left : int, right : int):
    """Adds two numbers together."""
    await bot.say(left + right)


async def _signout():
    if ctx.valid():
        print("Sending farewell message...")
        ipaddr = iotpi.get_ipaddr()
        await bot.send_message(ctx.channel, "Goodbye")
    print("Signing out...")
    await bot.close()
    print('Signed out')


def on_sigterm(signum, frame):
    print('Received signal ' + signum)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.ensure_future(_signout()))
    sys.exit(0)


# Set signal handlers
signal.signal(signal.SIGTERM, on_sigterm)

bot.run(config.discord_token)
