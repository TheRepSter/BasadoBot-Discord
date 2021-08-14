#Commands:
#   - binfo
#   - basado {[rec]user:Discord.user} {[def:None]pill:str}
#   - bmasbasados
#   - bcantidaddebasado {[def:userpost]user:Discord.user}
#   - btirarpildora {[rec]pill:str}

from discord.ext import commands

bot = commands.Bot(command_prefix="b")

@commands.command()
async def binfo():
    pass

@commands.command()
async def basado():
    pass

@commands.command()
async def bmasbasados():
    pass

@commands.command()
async def bcantidaddebasado():
    pass

@commands.command()
async def btirarpildora():
    pass


def run(token):
    bot.run(token)