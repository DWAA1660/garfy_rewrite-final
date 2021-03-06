import motor
from motor import motor_asyncio
from nextcord import SlashOption, ChannelType
from nextcord.abc import GuildChannel
import nextcord
from nextcord import Interaction, slash_command
from nextcord.ext import commands, application_checks

from bot import client, CLUSTER, Global_Report_Channel, Global_Log_Channel

global_report_channel = Global_Report_Channel
# global log channel
channel_id = Global_Log_Channel

cluster_local = CLUSTER

cluster = motor.motor_asyncio.AsyncIOMotorClient(cluster_local)
db = cluster["VenoxDB"]
collection = db["report_channels"]


class reports(commands.Cog):

    def __init__(self, client):
        self.client = client

    @application_checks.has_permissions(manage_guild=True)
    @slash_command(description="Setup the report command")
    async def reportsetup(self, interaction: Interaction,
                          report_channel: GuildChannel = SlashOption(channel_types=[ChannelType.text])):
        ctxchannel = interaction.channel.id
        channelfletched = await client.fetch_channel(ctxchannel)
        try:
            ctxguild_id = str(interaction.guild.id)
            data = {"_id": ctxguild_id, "guildid": ctxguild_id, "reports_id": report_channel.id}
            await collection.insert_one(data)
            await interaction.send("Report channel setup!")
        except:
            getting_replaced = await collection.find_one({"_id": ctxguild_id})
            await collection.replace_one(getting_replaced, data)
            await interaction.send("Replaced report channel")

    @slash_command(description="Report a user and get a response asap")
    async def report(self, interaction: Interaction, member: nextcord.Member, reason=None):
        try:
            # sending to global report channel

            global_channel = await client.fetch_channel(global_report_channel)
            await global_channel.send(
                f"`{interaction.user}` has reported `{member}` in `{interaction.guild.name}` in channel `{interaction.channel.name}` for reason `{reason}`")
            await interaction.send("Reported thank you", ephemeral=True)

            # sending to defined report channel

            ctxguild_id = str(interaction.guild.id)
            results = await collection.find_one({"_id": ctxguild_id})
            server_report_channel = await client.fetch_channel(results["reports_id"])
            em = nextcord.Embed(title="New report!", description=f"{interaction.user} has reported {member.name}", color=0xe37e00)
            em.add_field(name="Channel", value=interaction.channel.name)
            em.add_field(name="Reason", value=reason)
            await server_report_channel.send(embed=em)
            log_channel = await client.fetch_channel(channel_id)
            await log_channel.send(
                f"`{interaction.user}` has reported `{member}`  in channel `{interaction.channel.name}` for reason `{reason}`")
        except:
            await interaction.send("Report failed please notify staff", ephemeral=True)


def setup(client):
    client.add_cog(reports(client))
