import discord
import os
import random
from keep_alive import keep_alive

client = discord.Client()

insults = [
  "Baka!",
  "Trash!",
  "Stupid blonde!"
]

@client.event
async def on_ready():
  print('{0.user} has entered The Igloo'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith('!hello'):
    await message.channel.send('Hello!')
  if message.content.startswith('!darkness'):
    await message.channel.send(random.choice(insults))
  
keep_alive()
client.run(os.getenv('token'))