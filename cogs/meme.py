from nextcord.ext import commands
from nextcord import Interaction
from nextcord import slash_command
import nextcord
import copy
import json
import urllib

class MemeManager(nextcord.ui.View):
  def __init__(self, author):
    super().__init__()
    self.value = None
    self.author = author
    self.msg = None

  @nextcord.ui.button(label="Next Meme", style=nextcord.ButtonStyle.green)
  async def nextmeme(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
    if interaction.user == self.author:
      memeApi = urllib.request.urlopen('https://meme-api.herokuapp.com/gimme')
      memeData = json.load(memeApi)
      memeUrl = memeData['url']
      memeName = memeData['title']
      memePoster = memeData['author']
    
      embed=nextcord.Embed(title=memeName, color=0xe37d00)
      embed.set_image(url=memeUrl)
      embed.set_footer(text=f"Meme By: " + memePoster)
      self.embed = embed
      await self.msg.edit(embed=embed)
    else:
      await interaction.response.send_message("This isn't your button!", ephemeral=True)


  @nextcord.ui.button(label=" ", style=nextcord.ButtonStyle.gray)
  async def blank(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
    pass

  @nextcord.ui.button(label="Done", style=nextcord.ButtonStyle.red)
  async def done(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
    if interaction.user == self.author:
      await self.msg.edit(embed=self.embed, view=None)
    else:
      await interaction.response.send_message("This isn't your button!", ephemeral=True)

class Meme(commands.Cog):

    def __init__(self, client):
        self.client = client

    @slash_command()
    async def meme(self, interaction : Interaction):
      try:
        view = MemeManager(interaction.user)
        
        memeApi = urllib.request.urlopen('https://meme-api.herokuapp.com/gimme')
        memeData = json.load(memeApi)
        memeUrl = memeData['url']
        memeName = memeData['title']
        memePoster = memeData['author']
      
        embed=nextcord.Embed(title=memeName, color=0xe37d00)
        embed.set_image(url=memeUrl)
        embed.set_footer(text=f"Meme By: " + memePoster)
        await interaction.send(embed=embed, view=view)
      
        msg = None
        async for message in interaction.channel.history(limit=1):
          msg = message
        view.msg = msg
      except:
        pass
    

    
def setup(client):
  client.add_cog(Meme(client))
