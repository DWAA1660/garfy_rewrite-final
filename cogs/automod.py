from nextcord.ext import tasks, commands, application_checks
import nextcord
from nextcord import Interaction, SlashOption, ChannelType
from nextcord.abc import GuildChannel
from nextcord import slash_command
from better_profanity import profanity
import random
import json

#got it working :D

class automod(commands.Cog):

    def __init__(self, client):
        self.client = client

    # lemme copy + paste
    @application_checks.has_permissions(manage_messages=True)
    @slash_command()
    async def toggle_censor(self, interaction: Interaction):
        guild = interaction.guild.id
        guilds = eval(open("saving/automod.txt", "r").read())
        if not guild in guilds:
            guilds[guild] = False

        if guilds[guild] == False:
            guilds[guild] = True
            await interaction.send("Message Censoring Enabled")
        else:
            guilds[guild] = False
            await interaction.send("Message Censoring Disabled")

        open("saving/automod.txt", "w").write(str(guilds))


    @commands.Cog.listener()
    async def on_message(self, message):
      file = eval(open("saving/automod.txt", "r").read())
      if message.guild.id in file:
        if file[message.guild.id] == True:
            whitelist = ["kill"]
            custom_badwords = ['b!tch', 'sh¡t']
            profanity.add_censor_words(custom_badwords)
            if profanity.contains_profanity(message.content):
              await message.delete()
              await message.channel.send(f"Dont swear {message.author.mention}")







def setup(client):
    client.add_cog(automod(client))


    
