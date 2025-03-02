import discord  # 모듈 불러오기
import os
from dotenv import load_dotenv
from keep_alive import keep_alive

load_dotenv(verbose=True)

intents = discord.Intents.all()
client = discord.Client(intents=intents)
welcome_msg = "Hello Bot v0.1 is ready, jangjinone@gmail.com"

@client.event
async def on_ready():
    await client.get_channel(1343588295820443678).send(welcome_msg)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!"):
        cmd = message.content[1:]
        if cmd.startswith("안녕"):
            await message.channel.send("안녕하세요")
            await message.add_reaction("👍")
        elif cmd.startswith("이름"):
            await message.channel.send("jangjinone bot")
        else:
            await message.channel.send("안녕 <-- 이라고 치시면 안녕하세요라고 합니다.")

keep_alive()
client.run(os.getenv("DISCORD_TOKEN"))  # 봇 실행