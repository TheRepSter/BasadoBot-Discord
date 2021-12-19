import discord

messageInfo=discord.Embed(title="¡Hola! ¡Soy un bot llamado BasadoBot!", description="He sido creado por @RepSter#2681, por simple diversión.\nCuento \"basados\", es decir, cuando estás de acuerdo con una persona.\nTambién genero frases graciosas un poco cuñadas.\nLos comandos son los siguientes:", color=0xff0000)
messageInfo.add_field(name="/help", value="Muestra este mensaje.", inline=False)
messageInfo.add_field(name="/masbasados", value="Muestra el top 10 de basados.", inline=False)
messageInfo.add_field(name="/cantidaddebasado", value="Muestra los basados según el usuario.", inline=False)
messageInfo.add_field(name="/frasecunada", value="Envia una frase cuñada aleatoria.", inline=False)
messageInfo.add_field(name="/basado", value="Para basar a una persona.", inline=False)
messageInfo.set_footer(text="¿Tienes alguna duda? ¡Habla por MD con mi creador!")