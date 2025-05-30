import discord  # 모듈 불러오기
import os
import random
import asyncio  # 추가된 모듈
from dotenv import load_dotenv
from keep_alive import keep_alive

load_dotenv(verbose=True)

intents = discord.Intents.all()
client = discord.Client(intents=intents)
welcome_msg = "Hello Bot v0.1 is ready, jangjinone@gmail.com"

# 사용자 커스텀 명령어와 응답을 저장하는 딕셔너리
custom_commands = {}

@client.event
async def on_ready():
    await client.get_channel(1343588295820443678).send(welcome_msg)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!"):
        cmd = message.content[1:]  # 명령어에서 "!" 제거

        # 사용자 정의 명령어 처리
        if cmd.startswith("안녕"):
            await message.channel.send("안녕하세요")
            await message.add_reaction("👍")

        elif cmd.startswith("이름"):
            await message.channel.send("jangjinone bot")

        elif cmd.startswith("로또"):
            lucky_number = random.randint(1, 45)
            random_numbers = random.sample(range(1, 46), 3)

            await message.channel.send("🎰 행운의 숫자를 뽑고 있습니다...")
            await asyncio.sleep(1)

            await message.channel.send("🔢 당신의 숫자를 하나씩 공개합니다...")
            for i, num in enumerate(random_numbers, start=1):
                await asyncio.sleep(1.5)
                await message.channel.send(f"{i}번 숫자: **{num}**")

            await asyncio.sleep(1.5)
            await message.channel.send(f"🎰 행운의 숫자: **{lucky_number}**")

            if lucky_number in random_numbers:
                await asyncio.sleep(0.5)
                await message.channel.send("🎉 당첨! 🎉")
            else:
                await asyncio.sleep(0.5)
                await message.channel.send("😢 아쉽지만 다음 기회에!")

        elif cmd.startswith("가르치기"):
            # !가르치기 [명령어] [응답] 형식으로 처리
            parts = message.content.split(" ", 2)
            if len(parts) < 3:
                await message.channel.send("명령어와 응답을 입력해 주세요. 예시: !가르치기 [명령어] [응답]")
            else:
                custom_command = parts[1]
                response = parts[2]
                custom_commands[custom_command] = response
                await message.channel.send(f"새로운 명령어를 학습했습니다: **{custom_command}**")

        elif cmd in custom_commands:
            # 사용자 정의 명령어에 대해 응답
            await message.channel.send(custom_commands[cmd])

        else:
            await message.channel.send("안녕 <-- 이라고 치시면 안녕하세요라고 합니다.")

keep_alive()
client.run(os.getenv("DISCORD_TOKEN"))  # 봇 실행
