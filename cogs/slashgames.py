from nextcord.ext import commands
import nextcord
from nextcord import Interaction
from nextcord import slash_command
import _google as google
from better_profanity import profanity
from dadjokes import Dadjoke
import random
import randfacts


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
    async def google(self, interaction: Interaction, *, query):
        ignore = ["kill", "die", "death", "lmao", "len", "stupid", ]  # Ignores these words
        profanity.load_censor_words(whitelist_words=ignore)
        if profanity.contains_profanity(query):
            await interaction.send("That word is banned")

        else:
            embed = nextcord.Embed(title="Google Results For: " + query, url="https://google.com", description=" ",
                                       color=0x4d7cff)
            results = google.search(query)
            v = ""
            for r in results:
                v += f"{r}\n"

            embed.add_field(name="-----", value=v, inline=True)
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


    
