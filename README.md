# Discord.py第一章 機器人從建立到啟動
## 前言
早安，我是火柴，一個Github新手。這是一個只教你手搓Discord.py機器人的地方，原理或是更細的內容可能要看其他大佬的創作。  
Btw，東西是自己上網摸跟看ChatGPT後東拼西湊出來的產物，有需要改進的地方還請多多指教了<( _ _ )>

這篇會帶幾個主題，建議用`ctrl+F`搜尋底下的標籤，這樣比較好找需要的內容。  
- Discord Devloper前置作業
- VsCode前置作業
- 啟動Discord Bot  

## Discord Developer前置作業
1. 首先打開Discord開發者頁面[點我](https://discord.com/developers/docs/intro)
2. 登入後找到左上角的`applications`後點進去
   
   ![image](https://github.com/javaowo/Discord.py/blob/main/image/Applications.jpeg)
3. 找到右上角的`New Application`後點進去
   
   ![image](https://github.com/javaowo/Discord.py/blob/main/image/N_A.jpeg)
4. 幫它取個名，然後Create它 
   
   ![image](https://github.com/javaowo/Discord.py/blob/main/image/Create.jpeg)
5. 邀請機器人至伺服器  
   - 點擊左邊的`OAuth2`

   ![image](https://github.com/javaowo/Discord.py/blob/main/image/OAuth2.jpeg)  
   - 找到`OAuth2 URL Generator`中的`Bot`把它打勾起來

   ![image](https://github.com/javaowo/Discord.py/blob/main/image/bot.jpeg)
   底下這邊會叫你選權限，我有三個建議：
      #### 1. 不要勾選  
      若選擇不要勾選的話就不會有刪不掉的身份組，但需要手動給予機器人權限。  
      #### 2. 賦予管理員權限  
      這是最簡單的，在底下權限選取那裡的左上角`Adiministrator`打勾就好。  
      #### 3. 根據機器人功能選擇用得到的權限  
      這個到後期比較會知道你的機器人需要什麼功能，初學者較不建議使用這個選擇。  
這邊我先選擇賦予管理員權限，是最簡單的且不會有權限不足的問題，然後複製底下的邀請連結。  

  ![image](https://github.com/javaowo/Discord.py/blob/main/image/Administrator.jpeg)  
  之後到瀏覽器貼上，就可以邀請至你想要讓機器人進去的伺服器了（邀請者需有該伺服器的管理權限）  

  ![image](https://github.com/javaowo/Discord.py/blob/main/image/invite.jpeg)


這樣你就完成第一步：機器人的建置了。不過此時的機器人還不能使用，先不要急著把開發者網頁關掉，並接著下文繼續...  

## VsCode前置作業  
1. 下載VSCode[點我](https://code.visualstudio.com/)

   ![image](https://github.com/javaowo/Discord.py/blob/main/image/VScode_D.png)  
   下載下去後打開exe檔，然後就一直下一步下去到安裝完成就好
2. 打開VSCode，理論上會要先設定一些東西，就照著做就好
   接下來道延伸模組搜尋`python`並安裝
   > 如果覺得都是英文不習慣的話，也可以搜尋`Chinese`會有一個中文繁體包，安裝後介面就會變中文了

   ![image](https://github.com/javaowo/Discord.py/blob/main/image/Download.png)  
3. 確認python版本
   我們要使用的是3.11版本，首先使用ctrl+`打開終端機，然後輸入以下指令
   ```python
   pip --version python
   ```
   Enter後你會在下面一行看到python所處的位置和版本，如果最後面括號寫的是`python 3.11`那你就成功了

   ![image](https://github.com/javaowo/Discord.py/blob/main/image/Version.png)
4. 下載Discord.py  
   在終端機輸入以下程式碼，即可完成下載
   ```python
   pip install discord.py
   ```

## 啟動Discord Bot
我們還有一些步驟還沒完成，先讓我們回到開發者網站...[點我](https://discord.com/developers/docs/intro)
  
1. 找到你機器人的icon點進去，選擇旁邊的`Bot`

   ![image](https://github.com/javaowo/Discord.py/blob/main/image/Bot.png)
2. 找到中間的`Reset Token`，點下去

   ![image](https://github.com/javaowo/Discord.py/blob/main/image/Token.png)
3. 你會獲得一個Token，複製他，並且不要分享給別人（這是機器人的代碼）

   ![image](https://github.com/javaowo/Discord.py/blob/main/image/Copy.png)
4. 往下滑，找到`Privileged Gateway Intents`，並打勾下面的三個選項（圖片中沒有勾選）
     
   ![image](https://github.com/javaowo/Discord.py/blob/main/image/PGI.png)
5. 接下來新增一個檔案，語言選擇Python  
   可複製底下程式碼，並替換「YOUR_BOT_TOKEN」這個文字成剛剛複製的Token。  
   上面的Discord.py檔案有完整的程式碼解釋
```python
import discord

from discord.ext import commands

client = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    print(f'My ID is {client.user.id}')

client.run("YOUR_BOT_TOKEN")
```
最後按下右上角三角形的執行按鈕，理論上機器人就能正常運作了（雖然沒有任何功能）
  
