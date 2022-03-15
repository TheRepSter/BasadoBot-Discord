import discord
from discord.ext import commands
from discord import Option
from basadobotdiscord.embeds import messageInfo
from basadobotdiscord.models import User, session
from basadobotdiscord.views import ViewCuñado, ViewInfo
from basadobotdiscord.cunado import generador_frase
from time import time
intents = discord.Intents.default()
intents.members = True

discord.MemberCacheFlags.from_intents(intents=intents)

bot = commands.Bot(intents=intents)

#Slash commands.
@bot.slash_command(name="help", description="¿Necesitas ayuda? ¡Aquí te la dan!")
async def help(ctx):
    await ctx.respond(embed=messageInfo, view=ViewInfo())

@bot.slash_command(name="basado", description="Para basar a una persona.")
async def basado(ctx, member:Option(discord.Member, "El miembro que está basado", required=True, default=None)):
    if ctx.author.id == member.id:
        await ctx.respond("No puedes basarte a ti mismo...")
        return
        
    personaQueDaBasado = session.query(User).filter(User.userid == str(ctx.author.id), User.serverid == str(ctx.guild.id)).first()
    if not personaQueDaBasado:
        personaQueDaBasado = User(serverid = str(ctx.guild.id), userid = str(ctx.author.id), ultimobasado = 0, basados = 0)

    if time() - personaQueDaBasado.ultimobasado < 60:
        await ctx.respond("¡No puedes dar basados tan rápido!")
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
    await ctx.respond(f"Ahora {member.display_name} tiene {personaBasada.basados} basados.")

@bot.slash_command(name="másbasados", description="Muestra el top 10 de basados.")
async def masbasados(ctx):
    topBasado = discord.Embed(title="El Top 10 de los usuarios más basados en el servidor es actualmente:")
    usuarios = session.query(User).filter(User.serverid == str(ctx.guild.id)).order_by(User.basados.desc()).limit(10).all()
    if len(usuarios) == 0:
        topBasado.add_field(name="¡En este servidor no hay nadie basado!", value="Comienza a basar a gente para que aquí haya algo.")
    
    else:
        for numb, i in enumerate(usuarios):
            topBasado.add_field(name=str(numb+1), value=bot.get_user(int(i.userid)).display_name, inline=True)
    
    await ctx.respond(embed=topBasado)

@bot.slash_command(name="cantidaddebasado", description="Muestra los basados según el usuario.")
async def cantidaddebasado(ctx, member:Option(discord.Member, "El miembro que quieres saber", required=False, default=None)):
    if member == None:
        member = ctx.author
    usuarioServer = session.query(User).filter(User.userid == str(member.id), User.serverid == str(ctx.guild.id)).first()
    if not usuarioServer:
        usuarioServer = User(serverid = str(ctx.guild.id), userid = str(member.id), ultimobasado = 0, basados = 0)
        session.add(usuarioServer)
        session.commit()
    usuarioAll = session.query(User).filter(User.userid == str(member.id)).all()
    basadosTotales : int = 0
    for i in usuarioAll:
        basadosTotales += i.basados

    message = discord.Embed(title=member.display_name)
    message.add_field(name="Basados en este servidor:", value=usuarioServer.basados, inline=False)
    message.add_field(name="Basados totales:", value=basadosTotales, inline=False)
    await ctx.respond(embed=message)

@bot.slash_command(name="frasecuñada", description="Envia una frase cuñada aleatoria.")
async def frasecunada(ctx):
    message, links = generador_frase(ctx.author.display_name)
    await ctx.respond(content = message, view = ViewCuñado(ctx, ctx.author.display_name, links))

@bot.slash_command(name="enpesetas", description="Para ver cuantas pesetas son tantos euros.")
async def enpesetas(ctx, euros:Option(float, "Cantidad de euros.", required=True, default=None)):
    euros = abs(euros)
    cents = ""
    pesetas = euros * 166.3860
    perraGorda = pesetas * 10
    euros = f"{int(euros):,}" if int(euros) == float(euros) else f"{round(euros, 2):,.2f}"
    pesetas = f"{int(pesetas):,}" if int(pesetas) == float(pesetas) else f"{round(pesetas, 2):,.2f}"
    euros = euros.replace(",", "@").replace(".", ",").replace("@", ".")
    pesetas = pesetas.replace(",", "@").replace(".", ",").replace("@", ".")
    perraGordaTrunc = int(perraGorda)
    residuo = round((perraGorda - perraGordaTrunc) * 10)
    perraGordaTrunc = f"{perraGordaTrunc:,}".replace(",", ".")
    if residuo >= 5:
        cents += " con 1 perra chica"
        residuo -= 5
    if residuo == 1:
        cents += f" y {residuo} centimo"
        residuo -= 1
    if residuo != 0:
        cents += f" y {residuo} centimos"
    
    await ctx.respond(content = f"¿{euros}€? En mi epoca eso eran {pesetas} pesetas. Es decir, {perraGordaTrunc} perras gordas{cents}.")


def run(token):
    bot.run(token)