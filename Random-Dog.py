##Use the command !!dog in discord
###Used https://dev.to/mikeywastaken/discord-py-project-3-random-dog-pics-3b4a
import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
import aiohttp

client = commands.Bot(command_prefix="!!")
load_dotenv()
token = os.getenv('TOKEN')

@client.event
async def on_ready():
   print("Ready")

@client.command()
async def dog(ctx):
   async with aiohttp.ClientSession() as session:
      request = await session.get('https://some-random-api.ml/img/dog') # Make a request
      dogjson = await request.json() # Convert it to a JSON dictionary
   embed = discord.Embed(title="Doggo!", color=discord.Color.purple()) # Create embed
   embed.set_image(url=dogjson['link']) # Set the embed image to the value of the 'link' key
   await ctx.send(embed=embed) # Send the embed

client.run(token)