import asyncio
import os
import random
import time
import wavelink
import nextcord
from nextcord import slash_command, Interaction
from nextcord.ext import commands

TOKEN = os.getenv("TOKEN")
CLUSTER = os.getenv("CLUSTER")
Global_Report_Channel = os.getenv("Global_Report_Channel")
Global_Log_Channel = os.getenv("Global_Log_Channel")

intents = nextcord.Intents.default()
intents.members = True
client = commands.Bot(intents=intents)


@client.event
async def on_ready():
    print("bot is ready")
    tasks = [["Ryxs playground", "g"], [[f"{len(client.guilds)} servers"], "s"], ]
    ts = []
    for task in tasks:
        if task[1] == "g":
            ts.append(nextcord.Game(task[0]))
        elif task[1] == "s":
            ts.append(nextcord.Activity(type=nextcord.ActivityType.watching, name=task[0][0], ))
    while 1:
        for g in ts:
            await client.change_presence(status=nextcord.Status.online, activity=g)
            await asyncio.sleep(60)


@commands.Cog.listener()
async def on_wavelink_node_ready(self, node: wavelink.Node):
    print(f"node {node.identifier} is ready!!!")


async def node_connect(self):
    await client.wait_until_ready()
    await wavelink.NodePool.create_node(client=client,
                                        host='kerosine.darrennathanael.com',
                                        port=2124,
                                        password='SleepingOnTrains')


class Confirm(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None


async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')


async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(TOKEN)
