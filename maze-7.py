import pygame
import random
import sys
import time

# 初始化 Pygame
pygame.init()

# 常數設定
WIDTH, HEIGHT = 800, 800  # 視窗大小
GRID_SIZE = 25  # 迷宮規模 (25x25格子)
CELL_SIZE = WIDTH // GRID_SIZE  # 每個格子的像素大小
FPS = 60  # 畫面更新速率
# 顏色定義
WHITE = (255, 255, 255)  # 路徑
BLACK = (50, 50, 50)  # 牆壁
BLUE = (50, 50, 255)  # 玩家
GREEN = (55, 150, 50)  # 終點和結果文字
RED = (255, 150, 150)  # 統計和選項文字

# 迷宮生成及移動方向
DIRECTIONS = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # up, right, down, left

# 初始化遊戲畫面
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mouse and Keyboard Maze Escape")

# Font
font = pygame.font.Font(None, 36)  # 用於遊戲中顯示統計數據的字體
win_font = pygame.font.Font(None, 48)  # 用於勝利訊息的字體

# 生成迷宮，使用深度優先搜尋（DFS）演算法
def create_maze(grid_size):
    """Generates a maze using depth-first search."""
    maze = [[1] * grid_size for _ in range(grid_size)]  # 1 表示牆壁，0 表示路徑
    stack = [(0, 0)]  # 初始位置 (0, 0)
    maze[0][0] = 0  # 將起點設為路徑

    while stack:
        x, y = stack[-1]
        neighbors = []
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx * 2, y + dy * 2
            if 0 <= nx < grid_size and 0 <= ny < grid_size and maze[nx][ny] == 1:
                neighbors.append((nx, ny, dx, dy))

        if neighbors:
            nx, ny, dx, dy = random.choice(neighbors)
            maze[x + dx][y + dy] = 0  # 移除牆壁
            maze[nx][ny] = 0  # 新位置設為路徑
            stack.append((nx, ny))
        else:
            stack.pop()

    return maze

# 繪製迷宮
def draw_maze(maze):
    """Draws the maze on the screen."""
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            color = BLACK if maze[x][y] == 1 else WHITE
            pygame.draw.rect(screen, color, (y * CELL_SIZE, x * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# 繪製玩家
def draw_player(x, y):
    """Draws the player on the screen."""
    pygame.draw.rect(screen, BLUE, (y * CELL_SIZE, x * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# 繪製終點
def draw_end(x, y):
    """Draws the goal on the screen."""
    pygame.draw.rect(screen, GREEN, (y * CELL_SIZE, x * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# 在畫面左上角顯示計時與步數
def display_stats(time_elapsed, steps):
    """Displays time and steps on the screen."""
    stats_text = f"Time: {time_elapsed:.1f}s  Steps: {steps}"
    stats_surface = font.render(stats_text, True, RED)
    screen.blit(stats_surface, (10, 10))  # 顯示在左上角

# 顯示勝利訊息與選擇（重新開始或退出）
def display_end_options(time_taken, steps):
    """Displays the win message."""
    screen.fill(WHITE)
    win_text = f"You Win! Time: {time_taken:.1f} seconds, Steps: {steps}"
    text_surface = win_font.render(win_text, True, GREEN)
    screen.blit(
        text_surface,
        (WIDTH // 2 - text_surface.get_width() // 2, HEIGHT // 3 - text_surface.get_height() // 2),
    )
    option_text = "Press R to Replay or Q to Quit"
    option_surface = font.render(option_text, True, RED)
    screen.blit(
        option_surface,
        (WIDTH // 2 - option_surface.get_width() // 2, HEIGHT // 2),
    )
    pygame.display.update()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # 重新遊玩
                    return True
                elif event.key == pygame.K_q:  # 退出遊戲
                    return False


def main():
    while True:
        # 生成迷宮
        maze = create_maze(GRID_SIZE)
        player_x, player_y = 0, 0  # 起始位置
        end_x, end_y = GRID_SIZE - 1, GRID_SIZE - 1  # 終點位置

        # 遊戲變數
        clock = pygame.time.Clock()
        start_time = time.time()
        steps = 0

        running = True
        while running:
            screen.fill(WHITE)
            draw_maze(maze)
            draw_player(player_x, player_y)
            draw_end(end_x, end_y)

            # 計算脫逃時間
            time_elapsed = time.time() - start_time

            # 顯示統計數據
            display_stats(time_elapsed, steps)

            pygame.display.update()
            clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN: # 處理鍵盤事件
                    if event.key in (pygame.K_w, pygame.K_UP):  # Move up
                        new_x, new_y = player_x - 1, player_y
                    elif event.key in (pygame.K_s, pygame.K_DOWN):  # Move down
                        new_x, new_y = player_x + 1, player_y
                    elif event.key in (pygame.K_a, pygame.K_LEFT):  # Move left
                        new_x, new_y = player_x, player_y - 1
                    elif event.key in (pygame.K_d, pygame.K_RIGHT):  # Move right
                        new_x, new_y = player_x, player_y + 1
                    else:
                        continue

                    # Check for valid movement
                    if 0 <= new_x < GRID_SIZE and 0 <= new_y < GRID_SIZE and maze[new_x][new_y] == 0:
                        player_x, player_y = new_x, new_y
                        steps += 1

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = pygame.mouse.get_pos()
                    click_x, click_y = my // CELL_SIZE, mx // CELL_SIZE
                    if abs(click_x - player_x) + abs(click_y - player_y) == 1 and maze[click_x][click_y] == 0:
                        player_x, player_y = click_x, click_y
                        steps += 1

            # Check if player reached the goal
            if player_x == end_x and player_y == end_y:
                time_taken = time.time() - start_time
                running = False
        replay = display_end_options(time_taken, steps)
        if not replay:
            break       


if __name__ == "__main__":
    main()
