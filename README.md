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
   
   ![image]()
3. 找到右上角的`New Application`後點進去
   
   ![image]()
4. 幫它取個名

   ![image]()  
   然後Create它    

5. 邀請機器人至伺服器  
   - 點擊左邊的`OAuth2`

   ![image]()  
   - 找到`OAuth2 URL Generator`中的`Bot`把它打勾起來

   ![image]()
   底下這邊會叫你選權限，我有三個建議：
      #### 1. 不要勾選  
      若選擇不要勾選的話就不會有刪不掉的身份組，但需要手動給予機器人權限。  
      #### 2. 賦予管理員權限  
      這是最簡單的，在底下權限選取那裡的左上角`Adiministrator`打勾就好。  
      #### 3. 根據機器人功能選擇用得到的權限  
      這個到後期比較會知道你的機器人需要什麼功能，初學者較不建議使用這個選擇。  
這邊我先選擇賦予管理員權限，是最簡單的且不會有權限不足的問題，然後複製底下的邀請連結。  

  ![image]()  
  之後到瀏覽器貼上，就可以邀請至你想要讓機器人進去的伺服器了（邀請者需有該伺服器的管理權限）  

  ![image]()


這樣你就完成第一步：機器人的建置了。不過此時的機器人還不能使用，先不要急著把開發者網頁關掉，並接著下文繼續...  

## VsCode前置作業  
1. 下載VSCode[點我](https://code.visualstudio.com/)

   ![image]()  
   下載下去後打開exe檔，然後就一直下一步下去到安裝完成就好
2. 打開VSCode，理論上會要先設定一些東西，就照著做就好
   接下來道延伸模組搜尋`python`並安裝
   > 如果覺得都是英文不習慣的話，也可以搜尋`Chinese`會有一個中文繁體包，安裝後介面就會變中文了

   !image  
3. 確認python版本
   我們要使用的是3.11版本，首先使用ctrl+`打開終端機，然後輸入以下指令
   ```python
   pip --version python
   ```
   Enter後你會在下面一行看到python所處的位置和版本，如果最後面括號寫的是`python 3.11`那你就成功了  

   !image

## 啟動Discord Bot
我們還有一些步驟還沒完成，先讓我們回到開發者網站...[點我](https://discord.com/developers/docs/intro)  
1. 
新增一個檔案，語言選擇Python
```python
import discord

from discord.ext import commands

client = commands.Bot(command_prefix='!', intents=discord.Intents.all())

client.run("YOUR_BOT_TOKEN")
```

我們來逐一解釋程式碼：  
1. 調用Discord函式庫
2. 從Discord.py引入處理指令的模組  
3-1. 命名處理機器人的物件「client」  
3-2. 命名機器人的前綴指令符號「!」，可根據需求更改為自己想要的前綴符號（不限）  
3-3. 賦予機器人接收訊息的權限「intents」，其中「Intents.all」代表機器人能夠接收所有可用的訊息  
4. 起動機器人，記得先把「YOUR_BOT_TOKEN」替換成你的機器人的Token  
  
  ### 獲得Discord機器人的Token
  
