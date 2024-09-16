# Discord.py第一章 機器人從建立到啟動
## 前言
早安，我是火柴。這是一個只教你手作的Discord.py機器人的地方，東西也是我自己上網摸跟看ChatGPT後東拼西湊出來的產物，有需要改進的地方還請多多指教了m(_ _)m

這篇會帶幾個主題，建議用`ctrl+F`搜尋底下的標籤，這樣比較好找需要的內容。  
- Discord Devloper前置作業
- VsCode前置作業
- 啟動Discord Bot  

## Discord Developer前置作業
1. 首先打開Discord開發者頁面[點我](https://discord.com/developers/docs/intro)
2. 登入後找到左上角的`applications`後點進去
   
   ![image](https://github.com/javaowo/Discord.py/blob/main/IMG_1297.jpeg)
3. 找到右上角的`New Application`後點進去
   
   ![image](https://github.com/javaowo/Discord.py/blob/main/IMG_1298.jpeg)
4. 幫它取個名

   ![image](https://github.com/javaowo/Discord.py/blob/main/IMG_1299.jpeg)  
   然後Create它    

5. 邀請機器人至伺服器  
   - 點擊左邊的`OAuth2`

   ![image](https://github.com/javaowo/Discord.py/blob/main/IMG_1300.jpeg)  
   - 找到`OAuth2 URL Generator`中的`Bot`把它打勾起來

   ![image](https://github.com/javaowo/Discord.py/blob/main/IMG_1302.jpeg)
   底下這邊會叫你選權限，我有三個建議：  
      #### 1. 不要勾選  
      若選擇不要勾選的話就不會有刪不掉的身份組，但需要手動給予機器人權限。  
      #### 2. 賦予管理員權限  
      這是最簡單的，在底下權限選取那裡的左上角`Adiministrator`打勾就好。  
      #### 3. 根據機器人功能選擇用得到的權限  
      這個到後期比較會知道你的機器人需要什麼功能，初學者較不建議使用這個選擇。  

這邊我先選擇賦予管理員權限，是最簡單的且不會有權限不足的問題，然後複製底下的邀請連結。  

  ![image](https://github.com/javaowo/Discord.py/blob/main/IMG_1303.jpeg)  
  之後到瀏覽器貼上，就可以邀請至你想要讓機器人進去的伺服器了（邀請者需有該伺服器的管理權限）  

  ![image](https://github.com/javaowo/Discord.py/blob/main/IMG_1304.jpeg)


這樣你就完成第一步：機器人的建置了。不過此時的機器人還不能使用，請接著下文繼續...  

## VsCode前置作業  
1. 首先來到下載python的網頁[點我](https://www.python.org/downloads/)

   ![image](https://github.com/javaowo/Discord.py/blob/main/IMG_1305.jpeg)
2. 選擇**python3.11**
   > 3.12使用的程式碼會不同，可能會有未知bug（？）

## 啟動Discord Bot

