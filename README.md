# Discord.py 建立機器人
## 前言
早安，我是火柴。這是一個只教你手作的Discord.py機器人的地方，東西也是我自己上網摸跟看ChatGPT後東拼西湊出來的產物，有需要改進的地方還請多多指教了m(_ _)m

這篇會帶幾個主題，建議用`ctrl+F`搜尋底下的標籤，這樣比較好找需要的內容。  
- Discord Devloper前置作業
- VsCode前置作業
- 啟動Discord Bot  

## Discord Developer前置作業
1. 首先打開Discord開發者頁面[點我](https://discord.com/developers/docs/intro)
2. 找到左上角的`applications`後點進去
   
   ![alt 文字](https://cdn.discordapp.com/attachments/996685902397063169/1282874246334255206/image.png?ex=66e0f13e&is=66df9fbe&hm=e666d566d87cb759df4e8d299494af8c4869cbc06ff11a46f27149c3268f4080&)
3. 找到右上角的`New Application`後點進去
   
   ![alt 文字](https://cdn.discordapp.com/attachments/996685902397063169/1283214102847819787/IMG_1262.png?ex=66e22dc3&is=66e0dc43&hm=b23208ff361890e836e11e7a0de3f5e3a09ee2d65d7c2cb6ac852a2e18baa9cf&)
4. 幫它取個名

   ![alt 文字](https://media.discordapp.net/attachments/996685902397063169/1283214103170650142/IMG_1264.png?ex=66e22dc3&is=66e0dc43&hm=8bd8fb9886a7ce6dc3135083c15510b4197ad90a62e7d39ad875ae5f08712443&)  
   然後Create它    

5. 邀請機器人至伺服器  
   - 點擊左邊的`OAuth2`

   ![alt 文字](https://media.discordapp.net/attachments/996685902397063169/1283217338124079114/IMG_1265.png?ex=66e230c6&is=66e0df46&hm=43536c165addd7578815c928c40e01915c20bb4090a908e5ec729611a9bd41bc&)  
   - 找到螢幕中的`Bot`把它打勾起來

   ![alt 文字](https://media.discordapp.net/attachments/996685902397063169/1283218516505399316/IMG_1266.png?ex=66e231df&is=66e0e05f&hm=f0dbfdad3c9f0b3243f74950e0cb87719eede9338e8e06a365980f564b938541&)
   底下這邊會叫你選權限，我有三個建議：
     ##### 1. 不要勾選
      若選擇不要勾選的話就不會有刪不掉的身份組，但需要手動給予機器人權限。
     ##### 2. 賦予管理員權限
      這是最簡單的，在底下權限選取那裡的左上角`Adiministrator`打勾就好。
     ##### 3. 根據機器人功能選擇用得到的權限
      這個到後期比較會知道你的機器人需要什麼功能，初學者較不建議使用這個選擇。  

這樣你就完成第一步：機器人的建置了。不過此時的機器人還不能使用，請接著下文繼續...  

## VsCode前置作業