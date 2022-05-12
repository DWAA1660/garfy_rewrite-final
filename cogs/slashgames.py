from nextcord.ext import tasks, commands
from asyncio.tasks import wait_for
from sys import prefix
import nextcord
from nextcord import Interaction, SlashOption, ChannelType
from nextcord.abc import GuildChannel
from nextcord import slash_command
from googlesearch import search
from better_profanity import profanity
from dadjokes import Dadjoke
import random
import randfacts

import json

import urllib


#got it working :D

class slash(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    #example command so you can copy paste
    @slash_command()
    async def slashcommand(self, interaction : Interaction):
      await interaction.response.send_message("LOL EZZZ")
      
      #await ctx.respond("bruh")
    #Note to blackhole927: fix it later
    #@slash_command(guild_ids=[server])
    #async def randimage(self, interaction : Interaction):
    #  x = Image.open(requests.get("https://picsum.photos/500", stream=True).raw)
    #  x.save("resources/rimage.png")
    #  await interaction.response.send_message(file=nextcord.File("resources/rimage.png"))
    #can you test it?
    #helpfull nextcord examples with slash commands and stuff

    #this command is full working
    @slash_command()
    async def repeat(self, interaction : Interaction, message):
      await interaction.response.send_message(message)
    

    #this command is fully working
    @slash_command()
    async def kill(self,interaction : Interaction, person):
      deaths = ['blended by fan',
                            'chopped into soup',
                        'thrown off a cliff',
                        'roasted in space',
                        'your mom\'ed to oblivion',
                        'removed from existance',
                        'exploded',
                        'killed by a spoon',
                        'ejected from the ship',
                        'swallowed by a black hole']	
      insults = [
        'I love my job >:)',
        'Get ded newb',
        'Time to die :)',
        'I kill all things with a smile',
        'Murder is ||fun||',
        'I\'m the Imposter. But you won\'t live long enough to tell anyone.',
        'Has been impostered',
      ]	
        
      dies = (f'{random.choice(deaths)}')
      embed=nextcord.Embed(title=insults[random.randint(0, len(insults)-1)], description=person + ' was ' + dies)
      await interaction.send(embed=embed)


    #this command is fully working
    

    @slash_command()
    async def slap(self, interaction : Interaction, *, member="Member"):
      await interaction.send(f"{member} just got slapped by a fish https://tenor.com/view/fish-slap-w2s-slap-funny-sidemen-gif-20599048")

    @slash_command()
    async def google(self, interaction : Interaction, amount, *, query):
      embed = nextcord.Embed(title="Google Results For: "+query, url="https://google.com", description=" ", color=0x4d7cff)
      amount = int(amount)
      if amount > 10:
        amount = 10
      for i in search(query, tld="co.in", num=amount, stop=amount, pause=2):
        embed.add_field(name=query, value=i, inline=True)
      await interaction.send(embed=embed)



    @slash_command()
    async def qq(self, interaction : Interaction, *, person="your"):
      responsessize = [
                '8==>',
                '8===>',
                '8->',
                '8=========>',
                '8==========>',
                '*nothing*'
            ]		    


      res = (f'{random.choice(responsessize)}')
      embed=nextcord.Embed(title=person + " qq size is:", description=person +  ' qq size is ' + res)
      await interaction.send(embed=embed)



    @slash_command()
    async def meme(self, interaction : Interaction):
      memeApi = urllib.request.urlopen('https://meme-api.herokuapp.com/gimme')
      memeData = json.load(memeApi)
      memeUrl = memeData['url']
      memeName = memeData['title']
      memePoster = memeData['author']

      embed=nextcord.Embed(title=memeName, color=0x4287f5)
      embed.set_image(url=memeUrl)
      embed.set_footer(text=f"Meme By: " + memePoster)
      await interaction.send(embed=embed)

    @slash_command()
    async def dadjoke(self, interation : Interaction):
      dadjoke = Dadjoke()
      dj = dadjoke.joke
      dj = profanity.censor(dj)
      await interation.send(dj)
  
    @slash_command()
    async def funfact(self, interaction = Interaction):
      x = randfacts.get_fact()
      await interaction.send(x)




    #I just needed a space to do these secret commands

    @commands.Cog.listener()
    async def on_message(self, message):
      msg = message.content

      if msg[0:2] == ">.":
        nextid = msg.find(" ")

        if msg[2:nextid] == "tellraw":
          msg = msg[nextid+1:len(msg)]

          text = msg

          await message.channel.send("tellraw @a {\"text\" : \"" + text + "\"}")

  




def setup(client):
    client.add_cog(slash(client))


    