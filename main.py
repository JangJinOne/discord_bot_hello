import discord  # 모듈 불러오기
import os
import random
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

        elif cmd.startswith("로또"):
            lucky_number = random.randint(1, 45)  # 행운의 숫자 (1~45 사이)
            random_numbers = random.sample(range(1, 46), 3)  # 3개의 랜덤 숫자
            
            result_msg = f"🎰 행운의 숫자: **{lucky_number}**\n" \
                         f"🔢 당신의 숫자: {random_numbers}\n"

            if lucky_number in random_numbers:
                result_msg += "🎉 당첨! 🎉"
            else:
                result_msg += "😢 아쉽지만 다음 기회에!"

            await message.channel.send(result_msg)

        else:
            await message.channel.send("안녕 <-- 이라고 치시면 안녕하세요라고 합니다.")

keep_alive()
client.run(os.getenv("DISCORD_TOKEN"))  # 봇 실행
