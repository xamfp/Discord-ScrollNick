import discord
import asyncio
import time
import uuid
import threading

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!scrollnick'):
        client.loop.create_task(scrollNick(message))

async def scrollNick(message):
    nick = client.user.name.lower()
    while True:
        for i in range(len(nick)):
            new_nick = nick[:i] + nick[i].swapcase() + nick[i+1:]  
            await client.change_nickname(message.server.me, new_nick) 

token = input('API Token: ')
client.run(token ,bot=False)
