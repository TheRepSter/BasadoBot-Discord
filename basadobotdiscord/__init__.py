#Commands:
#   - binfo
#   - basado {[rec]user:Discord.user} {[def:None]pill:str}
#   - bmasbasados
#   - bcantidaddebasado {[def:userpost]user:Discord.user}
#   - btirarpildora {[rec]pill:str}

import discord
from discord.ext import commands

messages = {
            1:"Casa de cartas",
            5:"Árbol joven",
            10:"Silla de oficina",
            20:"Canasta de baloncesto (llena de arena)",
            35:"Luchador de sumo",
            50:"Fundación de hormigón",
            75:"Sequoia gigante",
            100:"Empire State Building",
            200:"Gran pirámide de Giza",
            350:"Edificio de ensamblaje de vehículos de la ESA",
            500:"Fábrica de Boeing Everett",
            750:"Monte Fuji", 
            1000:"Denali",
            2000:"Annapurna"}

messageInfo = "\n\n".join([
                    "¡Hola! ¡Soy un bot llamado BasadoBot!",
                    "He sido creado por u/TheRepSter, por simple diversión.",
                    "Cuento \"basados\", es decir, cuando estás de acuerdo con una persona.",
                    "También llevo la cuenta de las píldoras que tiene cada usuario.",
                    "Los comandos son los siguientes:",
                    "- /info: muestra este mensaje.",
                    "- /usuariosmasbasados (o /usuariosmásbasados): muestra el top 10 de basados.",
                    "- /cantidaddebasado \{username\}: muestra los basados según el username",
                    "- /tirarpildora \{píldora\}: tira la píldora que mencione el usuario que pone el comando",
                    ""
                    "Soy de código abierto, es decir, ¡puedes ver mi código e incluso aportar!",
                    "[Haz click aquí para ver el código.](https://github.com/TheRepSter/BasadoBot-Discord)",
                    "¿Tienes alguna duda? ¡Háblame por MD a mi o a mi creador!"
                ]) 

bot = commands.Bot(command_prefix="b")

@commands.command(name="info")
async def info(ctx):
    await ctx.send(messageInfo)

@commands.command()
async def asado(ctx, member: discord.Member, pill:str):
    pass

@commands.command()
async def masbasados(ctx):
    pass

@commands.command()
async def cantidaddebasado(ctx):
    pass

@commands.command()
async def tirarpildora(ctx, pill:str):
    pass


def run(token):
    bot.run(token)