import nextcord
from nextcord import Interaction, slash_command
from nextcord.ext import commands, application_checks

from bot import client, Global_Report_Channel, Global_Log_Channel

global_report_channel = Global_Report_Channel
# global log channel
channel_id = Global_Log_Channel


class kick(commands.Cog):

    def __init__(self, client):
        self.client = client

    @application_checks.has_permissions(kick_members=True)
    @slash_command(description="Kick a member")
    async def kick(self, interaction: Interaction, member: nextcord.User, *, reason=None):
        if interaction.user == member:
            await interaction.send("Dont kick urself bozo")
        else:
            try:
                await member.kick(reason=reason)
            except nextcord.DiscordException as e:
                await interaction.response.send_message(f"Could not kick user: {member.mention}\n**Error:** `{str(e)}`", ephemeral=True)

            log_channel = await client.fetch_channel(channel_id)
            await log_channel.send(f" `{member}` has been kicked for reason `{reason}`")

            try:
                await member.send(f"You have been kicked for {reason}")
            except nextcord.DiscordException as e:
                await interaction.response.send_message(f"Could not send a message to user: {member.mention}\n**Error:** `{str(e)}`", ephemeral=True)

            em = nextcord.Embed(title='Member kicked', description=f"{member.name} was kicked for {reason}")

            await interaction.send(embed=em)


def setup(client):
    client.add_cog(kick(client))
