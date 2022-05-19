from nextcord.ext import commands
from nextcord import Interaction
from nextcord import slash_command
import nextcord
import copy


class suggestform(nextcord.ui.Modal):
  def __init__(self, client):
    super().__init__("Suggest Something")
    self.client = client

    self.a = nextcord.ui.TextInput(
      label="What do you want to suggest?",
      placeholder="suggestion here",
      required=True,
      max_length=1800,
    )
    
    self.b = nextcord.ui.TextInput(
      label="Why do you think its a good suggestion?",
      placeholder="you type here i think",
      required=True,
      max_length=1800,
    )

    self.add_item(self.a)
    self.add_item(self.b)

  async def callback(self, interaction: nextcord.Interaction) -> None:
    name = f"Suggestion from {interaction.user.name}"
    d = "**Idea**\n" + self.a.value
    embed = nextcord.Embed(title=name, description=d, color=0xe37d00)
    embed.add_field(name="Why?", value=self.b.value)
    
    c = await self.client.fetch_channel(931303714608803920)
    await c.send(embed=embed)


class suggestions(commands.Cog):

    def __init__(self, client):
        self.client = client

    @slash_command()
    async def suggest(self, interaction: nextcord.Interaction):
      modal = suggestform(self.client)
      await interaction.response.send_modal(modal)
    

    
def setup(client):
  client.add_cog(suggestions(client))
