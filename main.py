import discord  # 모듈 불러오기
import os
from keep_alive import keep_alive

TOKEN = "MTM0NTU5MTg3MDQ5MDgwNDI4NA.GjD7i_.JFi02GX7cX-GwheKXVKuvo0kQ8GuCOZC1xZZjg"  # 본인의 토큰을 여기에 넣어주세요.
CHANNEL_ID = '1343588295820443678'

class MyClient(discord.Client):
    async def on_ready(self):  # 봇이 준비되었을 때 실행되는 이벤트
        channel = self.get_channel(int(CHANNEL_ID))
        print("봇 준비완료")
        await channel.send(f"봇이 준비 완료되었습니다. 제 이름은 {client.user} 입니다")
        await channel.send(f"제작: 장진원, v0.1(2025-03-02)")
        print("==================================")

    async def on_message(self, message):  # 메시지가 도착할 때 실행되는 이벤트
        print(f"받은 메시지: {message.content}")  # 메시지 내용 로그 출력
        if message.author == client.user:  # 봇 자신에게는 반응하지 않도록 설정
            return
        if message.content == "안녕":
            print("응답: 안녕하세요")  # 응답 메시지 로그 출력
            await message.channel.send("안녕하세요")
        else:
            await message.channel.send("안녕 <--- 이라고 보내시면 제가 안녕하세요 합니다.")

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
keep_alive()
client.run(TOKEN)  # 봇 실행