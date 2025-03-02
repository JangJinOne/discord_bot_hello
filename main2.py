import discord
from discord.ext import commands
import asyncio
import os

from dotenv import load_dotenv
from keep_alive import keep_alive

load_dotenv(verbose=True)

# 학살단 서버 아이디
HK_GUILD_ID = 1247959509201326190

# ✅ 인텐트 설정
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    try:
        synced = await bot.tree.sync()
        print(f"✅ {len(synced)}개의 명령어가 동기화되었습니다!")
    except Exception as e:
        print(f"⚠️ 명령어 동기화 실패: {e}")

# ✅ `/감지` 명령어: 자신의 서버에 있는 멤버 중 HK 서버에 가입된 멤버 표시
@bot.tree.command(name="감지", description="자신의 서버에 가입된 멤버 중 HK 서버에 가입된 멤버를 표시합니다.")
async def detect_hk_members(interaction: discord.Interaction):
    print("🛠️ 감지 명령어 실행됨!")

    # 자신의 서버 가져오기
    guild = interaction.guild
    await guild.chunk()

    if not guild:
        await interaction.response.send_message("❌ 현재 서버를 찾을 수 없습니다.", ephemeral=True)
        return

    # 자신의 서버 멤버 중 HK 서버에 가입된 멤버 찾기
    hk_members_in_server = []

    try:
        # 모든 멤버를 순차적으로 확인
        for member in guild.members:
            print(f"member:{member}")
            print(f"mutual_guilds:{member.mutual_guilds}")

            member = await guild.fetch_member(member.id)
            
            # 해당 멤버가 HK 서버에 가입되어 있는지 확인
            if HK_GUILD_ID in [guild.id for guild in member.mutual_guilds]:
                hk_members_in_server.append(member.name)

            # 디버깅 로그: 멤버 처리 중
            if len(hk_members_in_server) % 10 == 0:  # 매 10번째 멤버마다 로그를 찍어서 확인
                print(f"처리된 멤버 수: {len(hk_members_in_server)}")

        if not hk_members_in_server:
            await interaction.response.send_message("❌ 현재 서버에 HK 서버에 가입된 멤버가 없습니다!", ephemeral=True)
            print("⚠️ HK 서버에 가입된 멤버가 없음")
            return

        # HK 서버에 가입된 멤버가 있으면 그 목록과 수를 출력
        member_count = len(hk_members_in_server)
        member_list = "\n".join(hk_members_in_server[:20])  # 최대 20명까지 출력
        await interaction.response.send_message(f"🔍 **HK 서버에 가입된 멤버 목록 (총 {member_count}명):**\n```\n{member_list}\n```")

    except asyncio.TimeoutError:
        await interaction.response.send_message("❌ 처리 시간이 너무 길어졌습니다. 다시 시도해주세요.", ephemeral=True)
        print("⚠️ 명령어 처리 시간 초과")
    except Exception as e:
        await interaction.response.send_message(f"❌ 오류가 발생했습니다: {str(e)}", ephemeral=True)
        print(f"⚠️ 오류 발생: {str(e)}")

# ✅ `/sync` 명령어: Slash Command 강제 동기화
@bot.tree.command(name="sync", description="Slash Command를 강제로 동기화합니다.")
async def sync_commands(interaction: discord.Interaction):
    try:
        synced = await bot.tree.sync()
        await interaction.response.send_message(f"✅ {len(synced)}개의 명령어가 동기화되었습니다!", ephemeral=True)
        print(f"✅ {len(synced)}개의 명령어가 강제 동기화됨!")
    except Exception as e:
        await interaction.response.send_message(f"⚠️ 명령어 동기화 실패: {e}", ephemeral=True)
        print(f"⚠️ 명령어 동기화 실패: {e}")

# ✅ 봇 실행
keep_alive()
bot.run(os.getenv("DISCORD_TOKEN2"))
