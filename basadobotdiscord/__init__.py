#Commands:
#   - binfo
#   - basado {[rec]user:Discord.user} {[def:None]pill:str}
#   - bmasbasados
#   - bcantidaddebasado {[def:userpost]user:Discord.user}
#   - btirarpildora {[rec]pill:str}

import discord
from discord.ext import commands
from basadobotdiscord.models import User, session
from basadobotdiscord.cunado import generador_frase
from time import time
intents = discord.Intents.default()
intents.members = True

discord.MemberCacheFlags.from_intents(intents=intents)

messageInfo=discord.Embed(title="¡Hola! ¡Soy un bot llamado BasadoBot!", description="He sido creado por @RepSter#2681, por simple diversión.\nCuento \"basados\", es decir, cuando estás de acuerdo con una persona.\nTambién llevo la cuenta de las píldoras que tiene cada usuario.\nLos comandos son los siguientes:", color=0xff0000)
messageInfo.set_author(name="BasadoBot", url="https://github.com/TheRepSter/BasadoBot-Discord")
messageInfo.add_field(name="b!info o b!help", value="Muestra este mensaje.", inline=False)
messageInfo.add_field(name="b!masbasados", value="Muestra el top 10 de basados.", inline=False)
messageInfo.add_field(name="b!cantidaddebasado", value="Muestra los basados según el username.", inline=False)
messageInfo.add_field(name="b!frasecunada", value="Envia una frase de cuñado aleatoria.", inline=False)
messageInfo.add_field(name="b!basado", value="Para basar a una persona", inline=False)
messageInfo.add_field(name="Soy de código abierto, es decir, ¡puedes ver mi código e incluso aportar!", value=" ¡Dale click arriba del todo y entrarás en mi github!", inline=False)
messageInfo.set_footer(text="¿Tienes alguna duda? ¡Habla por MD con mi creador!")

bot = commands.Bot(command_prefix="b!", help_command=None, intents=intents)

@bot.command(name="info", aliases=["help"])
async def info(ctx):
    await ctx.send(embed=messageInfo)

@bot.command(name="basado")
async def basado(ctx, member: discord.Member = None):
    if member == None:
        await ctx.send("Tienes que poner algun miembro.")
        return

    if ctx.message.author.id == member.id:
        await ctx.send("Eres tonto.")
        return
        
    personaQueDaBasado = session.query(User).filter(User.userid == str(ctx.message.author.id), User.serverid == str(ctx.guild.id)).first()
    if not personaQueDaBasado:
        personaQueDaBasado = User(serverid = str(ctx.guild.id), userid = str(ctx.message.author.id), ultimobasado = 0, basados = 0)

    if time() - personaQueDaBasado.ultimobasado < 60:
        await ctx.send("¡No puedes dar basados tan rápido!")
        personaQueDaBasado.ultimobasado = time()
        session.add(personaQueDaBasado)
        session.commit()
        return
    
    personaQueDaBasado.ultimobasado = time()

    personaBasada = session.query(User).filter(User.userid == str(member.id), User.serverid == str(ctx.guild.id)).first()
    if not personaBasada:
        personaBasada = User(serverid = str(ctx.guild.id), userid = str(member.id), ultimobasado = 0, basados = 0)

    personaBasada.basados += 1
    
    session.add(personaQueDaBasado)
    session.add(personaBasada)
    session.commit()
    await ctx.send(f"Ahora {member.display_name} tiene {personaBasada.basados} basados.")

@bot.command(name="masbasados", aliases=["másbasados", "topbasados"])
async def masbasados(ctx):
    topBasado = discord.Embed(title="El Top 10 de los usuarios más basados en el servidor es actualmente:")
    usuarios = session.query(User).filter(User.serverid == str(ctx.guild.id)).order_by(User.basados.desc()).limit(10).all()
    for numb, i in enumerate(usuarios):
        topBasado.add_field(name=str(numb+1), value=bot.get_user(int(i.userid)).display_name, inline=True)
    
    await ctx.send(embed=topBasado)

@bot.command()
async def cantidaddebasado(ctx, member: discord.Member = None):
    if member == None:
        member = ctx.message.author
    usuarioServer = session.query(User).filter(User.userid == str(member.id), User.serverid == str(ctx.guild.id)).first()
    if usuarioServer:
        usuarioAll = session.query(User).filter(User.userid == str(member.id)).all()
        basadosTotales : int = 0
        for i in usuarioAll:
            basadosTotales += i.basados

        message = discord.Embed(title=member.display_name)
        message.add_field(name="Basados en este servidor:", value=usuarioServer.basados, inline=False)
        message.add_field(name="Basados totales:", value=basadosTotales, inline=False)
        await ctx.send(embed=message)
    else:
        await ctx.send("Este usuario no existe")

@bot.command(name="frasecunada",aliases=["frasecunado", "frasecuñado", "frasecuñada","frasedecunada","frasedecunado", "frasedecuñado", "frasedecuñada"])
async def frasecunada(ctx):
    await ctx.send(generador_frase(ctx.message.author.display_name))

def run(token):
    bot.run(token)