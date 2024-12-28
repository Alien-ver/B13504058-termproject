import pygame
import random
import time

# 初始化 Pygame
pygame.init()

# 畫面設定
WIDTH, HEIGHT = 600, 600
ROWS, COLS = 25, 25  # 迷宮大小
CELL_SIZE = WIDTH // COLS
FPS = 60

# 顏色設定
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# 初始化畫面
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("滑鼠移動迷宮")
clock = pygame.time.Clock()

# 隨機生成迷宮
def generate_maze(rows, cols):
    maze = [[1 for _ in range(cols)] for _ in range(rows)]
    stack = [(0, 0)]
    visited = set(stack)

    while stack:
        x, y = stack[-1]
        maze[y][x] = 0
        neighbors = []

        for dx, dy in [(0, 2), (2, 0), (0, -2), (-2, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < cols and 0 <= ny < rows and (nx, ny) not in visited:
                neighbors.append((nx, ny))

        if neighbors:
            nx, ny = random.choice(neighbors)
            stack.append((nx, ny))
            visited.add((nx, ny))
            maze[(y + ny) // 2][(x + nx) // 2] = 0
        else:
            stack.pop()

    return maze

# 繪製迷宮
def draw_maze(maze, player_pos, goal_pos, steps, elapsed_time):
    for y in range(ROWS):
        for x in range(COLS):
            color = WHITE if maze[y][x] == 0 else BLACK
            pygame.draw.rect(screen, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # 繪製玩家
    px, py = player_pos
    pygame.draw.rect(screen, GREEN, (px * CELL_SIZE, py * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # 繪製終點
    gx, gy = goal_pos
    pygame.draw.rect(screen, BLUE, (gx * CELL_SIZE, gy * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # 顯示計時器與步數
    font = pygame.font.SysFont("Arial", 24)
    time_text = font.render(f"時間: {elapsed_time:.1f} 秒", True, RED)
    steps_text = font.render(f"步數: {steps}", True, RED)
    screen.blit(time_text, (10, 10))
    screen.blit(steps_text, (10, 40))

# 主程式
def main():
    maze = generate_maze(ROWS, COLS)
    player_pos = [0, 0]
    goal_pos = [COLS - 1, ROWS - 1]
    running = True
    steps = 0  # 記錄步數
    start_time = time.time()  # 計時開始

    while running:
        elapsed_time = time.time() - start_time  # 計算經過時間
        screen.fill(BLACK)
        draw_maze(maze, player_pos, goal_pos, steps, elapsed_time)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # 滑鼠點擊移動玩家
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                target_x, target_y = mouse_x // CELL_SIZE, mouse_y // CELL_SIZE

                # 確保目標格在相鄰範圍內且可移動
                if (
                    abs(target_x - player_pos[0]) + abs(target_y - player_pos[1]) == 1
                    and maze[target_y][target_x] == 0
                ):
                    player_pos = [target_x, target_y]
                    steps += 1

        # 檢測勝利
        if player_pos == goal_pos:
            print(f"恭喜你逃出迷宮！總步數: {steps}, 用時: {elapsed_time:.1f} 秒")
            show_victory_screen(steps, elapsed_time)
            running = False

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

# 顯示勝利畫面
def show_victory_screen(steps, elapsed_time):
    screen.fill(WHITE)
    font = pygame.font.SysFont("Arial", 36)
    message = f"恭喜！用時 {elapsed_time:.1f} 秒，步數: {steps}"
    text = font.render(message, True, GREEN)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
    pygame.display.flip()
    time.sleep(3)  # 停留 3 秒後關閉

if __name__ == "__main__":
    main()
