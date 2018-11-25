import asyncio
import aiohttp
from discord import Game
from discord.ext.commands import Bot
from chatterbot import ChatBot

chatbot = ChatBot(
    'WeafAi',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)

BOT_PREFIX = ("!!")
TOKEN = "TOKEN"  

client = Bot(command_prefix=BOT_PREFIX)
    
@client.event
@asyncio.coroutine
async def on_message(message):

    if message.content.startswith(BOT_PREFIX):
        respond = message.content
        requestBot = chatbot.get_response(respond)
        await client.send_message(message.channel,"Elias: " + str(requestBot))

@client.event
async def on_ready():
    await client.change_presence(game=Game(name="Overwatch"))
    print("Logged in as " + client.user.name)


async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers:")
        for server in client.servers:
            print(server.name)
        await asyncio.sleep(600)


client.loop.create_task(list_servers())
client.run(TOKEN)
