from nextcord import Interaction, SlashOption, ChannelType, slash_command, guild, Guild, components, TextInput
from nextcord.abc import GuildChannel
import nextcord
from nextcord import Interaction, slash_command
from nextcord.ext import commands, application_checks

from bot import client, CLUSTER, Global_Report_Channel, Global_Log_Channel

global_report_channel = Global_Report_Channel
# global log channel
channel_id = Global_Log_Channel


class info(commands.Cog):

    def __init__(self, client):
        self.client = client





    @slash_command(description="Sends link to support server")
    async def support(self, interaction: Interaction):
        await interaction.response.send_message('Join our support server https://discord.gg/kaddCVeRj6')

    @slash_command(description="Sends the number of guilds Venox is in")
    async def guilds(self, interaction: Interaction):
        guildamount = 1
        em = nextcord.Embed(title="Garfy\'s Guilds", description="Here is a list of servers that have garfy!", color=0xe37e00)
        for guild in client.guilds:
            em.add_field(name=f'Server {guildamount}', value=f'{guild.name}')
            guildamount += 1
        await interaction.send(f"Garfy is in {len(client.guilds)} servers", embed=em)


def setup(client):
    client.add_cog(info(client))
