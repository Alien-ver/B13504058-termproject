# MazeEscape: Bet Maze Escape

Welcome to the Maze Game: Bet Maze Escape!
This README provides a comprehensive overview of the game,
including its features, usage, architecture, development process, 
and customization options.

## (1) 遊戲功能 Features
Maze Game 具有以下功能：
- **隨機迷宮生成**：每次啟動遊戲時都會創建一個全新的迷宮。
- **多種操作方式**：可使用鍵盤方向鍵或滑鼠進行移動。
- **動態更新**：玩家每移動一次，更新畫面。
- **時間與步數記錄**：實時顯示玩家的完成時間與步數。
- **勝利訊息**：到達終點後顯示完成時間、步數與剩餘賭注。
- **小賭怡情**：玩家可在遊戲開始輸入起始賭注金額，並透過時間內通關來獲得賭金與繼續遊戲的資格。
- **顯示重新遊玩選項**：提供重新遊玩(R)或退出遊戲(Q)的選項

## (2) 使用方式 Usage

### 1. 設定環境

請確保您的系統已安裝 Python 和 pygame 。
以下是安裝所需步驟：
```bash
# 創建虛擬環境
python -m venv mazeescape-env

# 啟用虛擬環境
# On Windows:
source mazeescape-env\Scripts\activate
# On macOS/Linux:
source mazeescape-env/bin/activate

# 安裝pygame
pip install pygame
```

### 2. 啟動遊戲

```python
# 直接執行程式即可啟動遊戲：
python maze_escape.py
```
接著在TERMINAl輸入初始賭注金額即可開始挑戰

### 3. 遊戲玩法
執行程式後，您將看到一個隨機生成的迷宮，目標是在限制時間內從起點（左上角）移動到終點（右下角）。

起始限制時間：90秒

- **操作方式**：
 - 輸入初始賭注金額
 - 使用鍵盤或滑鼠控制又上藍色小方格
  - W/↑：向上移動
  - S/↓：向下移動
  - A/←：向左移動
  - D/→：向右移動
    (W/A/S/D請以英文輸入法進行)
  - 滑鼠點擊：移動到相鄰的白色方格


在迷宮中移動時，左上角會顯示您的已花費時間、步數、此局賭注金額及限制時間。

成功在時間內抵達終點後，畫面會顯示一條勝利訊息，包括完成此迷宮所花費的時間、總移動步數和目前總金額，以及是否重新遊玩的選項，按R可重玩、Q退出遊戲。

每贏一次下一次的挑戰時間會降低5秒，直到剩30秒時遊戲結束，您徹底贏了。

如果失敗(超過限制時間)則遊戲結束，則賭注會被拿走，直到賭注歸零即代表您輸了。

### 4. 客製化修改參數
若您想自訂迷宮大小，可調整以下程式碼中的參數：
```python
# 常數
WIDTH, HEIGHT = 750, 750  # 視窗大小
GRID_SIZE = 25  # 迷宮大小 (25*25)
FPS = 60  # 畫面更新速度（預設為 60 幀）
```


## (3) 程式的架構 Program Architecture
此project的檔案結構如下：
```
MazeEscape/
├── maze_escape.py   # 主遊戲腳本
└── README.md        # 文件說明
```
- **核心組成**：
 - create_maze：使用深度優先搜索算法生成迷宮
 - draw_maze：繪製迷宮的牆壁與路徑
 - draw_player：繪製玩家
 - draw_end：繪製終點
 - display_stats：在畫面左上角顯示計時與步數
 - display_end_options：顯示訊息與選擇（重新開始或退出）
 - main：處理遊戲邏輯與事件循環


## (4) 開發過程 Development Process

遊戲開發過程如下：
1. **靈感來源**：來自於小時候喜歡的遊戲：小精靈吃豆子
2. **需求規劃**：設計遊戲功能，包括鍵盤和滑鼠的雙重控制，並選擇 Pygame 作為繪圖與輸入的處理工具，同時加入計算移動步數與時間的功能。
3. **迷宮生成**：在詢問ChatGPT後使用深度優先搜尋演算法(depth-first search algorithm)生成隨機迷宮。
4. **玩家移動**：開發能同時支援鍵盤和滑鼠輸入移動的程式碼，並檢查是否進行有效移動。
5. **顯示圖形與數據**：ChatGPT協助撰寫相關代碼，使用 Pygame 繪製遊戲畫面，並在左上角顯示計時器與移動步數。
6. **測試與優化-1**：測試不同大小的迷宮、輸入模式與顯示顏色等等，確保遊戲流暢性與穩定性並加強色彩。
7. **程式改進-1**：細項部分修改，增加遊戲結束後的是否重新遊玩選項(以英文顯示)，並修改文字間距使其不與You win!的文字重疊。 
8. **程式改進-2**：在W/A/S/D外另加上上下左右箭頭鍵的控制選項，提升玩家自由度。
9. **程式改進-3**：加入課程所學的bet程式碼，增強遊戲體驗。
10. **測試與優化-2**：經過多次測試，發現最合適的起始限制與最低限制時間分別為90秒與30秒。


## (5) 參考資料來源 References
1. [小精靈](https://g.co/kgs/tsfw7wU) - 靈感來源
2. [ChatGPT](https://openai.com/index/chatgpt/) - 協助涉及pygame的程式碼書寫與。對話內容如下：
   - 如何使用python生成隨機迷宮
   - 如何使用Pygame將迷宮繪製為圖形化介面
   - 如何允許玩家使用鍵盤控制角色移動
   - 如何讓鍵盤跟滑鼠可以同時操控角色移動


## (6) 程式修改或增強的內容 Enhancements and Contributions

1. **計時與步數**：根據開始時間與結束時間計算花費時間，並在遊戲結束後顯示
2. **重新遊玩選項**：結合上課所學的迴圈與原程式中的代碼，在display_end_options中添加選項文字與While迴圈並使其顯示。並調整間距使其不與上方文字重疊
3. **箭頭鍵移動**：仿照pygame.K_w的邏輯加入pygame.K_UP等能用箭頭鍵控制的選項，並將原本的==修改為能同時監測W/A/S/D和箭頭鍵的in
4. **調整顯示顏色**：將牆面及方塊顏色等調整為為我認為較舒適的顏色，但玩家也能在程式執行前透過修改顏色變數製作自己喜歡的配色
5. **賭注遊戲**：賭注的部分是我融合課程所學到的賭場翻倍押注程式改編的，為了能增加遊戲的刺激與趣味性，將迷宮遊戲加上投注賭金的part
6. **改善顯示頁面**：使用\n將原本超出顯示螢幕的文字訊息格行顯示，使畫面較一目了然。

This README is made by myself.
We encourage further modifications and look forward to 
community contributions to improve Bet Maze Escape further.

