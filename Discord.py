# 調用Discord函式庫
import discord

# 從Discord.py引入處理指令的模組
from discord.ext import commands

"""
1. 命名處理機器人的物件「client」  
2. 命名機器人的前綴指令符號「!」，可根據需求更改為自己想要的前綴符號（不限）  
3. 賦予機器人接收訊息的權限「intents」，其中「Intents.all」代表機器人能夠接收所有可用的訊息  
"""
client = commands.Bot(command_prefix='!',intents=discord.Intents.all())

"""
1. 使用一個事件處理器
2. 當機器人完全啟動並連接到Discord的時候，打印已登入的機器人名稱和ID
"""
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    print(f'My ID is {client.user.id}')

# 起動機器人，記得先把「YOUR_BOT_TOKEN」替換成你的機器人的Token 
client.run("MTI4NTA2NzIzNDE3MTAyNzQ5Ng.GxJybq.UdlNLaAwxUObr86-mW4huKG7kXa2t23SIfIn6s")