import discord
from discord.ui import View, Button
from basadobotdiscord.cunado import generador_frase

timeoutDef = 60*60*24*365*20 # 20 años

class ViewInfo(View):
    def __init__(self):
        super().__init__(timeout=timeoutDef)
        self.add_item(Button(label="Código fuente", url="https://github.com/TheRepSter/BasadoBot-Discord"))

class ViewCuñado(View):
    def __init__(self, ctx, user, links):
        super().__init__(timeout=timeoutDef)
        self.ctx = ctx
        self.userIni = user
        for name, link in links.items():
            self.add_item(Button(label=name, url=link))

    @discord.ui.button(label="Dame más", custom_id="Dame")
    async def masFrases(self, button, interaction):
        if button.custom_id == "Dame":
            for i in self.children:
                if i.url != "" and i.url != None:
                    self.remove_item(i)

            message, links = generador_frase(self.userIni)
            for name, link in links.items():
                self.add_item(Button(label=name, url=link)) 

            await interaction.response.edit_message(content=message, view=self)

    @discord.ui.button(label="¡Guardar la frase!", style=discord.ButtonStyle.green)
    async def guardarFrase(self, button, interaction):
        self.remove_item([x for x in self.children if x.custom_id == "Dame"][0])
        self.remove_item(button)
        await interaction.response.edit_message(view=self)