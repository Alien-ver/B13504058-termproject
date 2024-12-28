import pygame
import random

# 初始化 Pygame
pygame.init()

# 畫面設定
WIDTH, HEIGHT = 600, 600
ROWS, COLS = 15, 15
CELL_SIZE = WIDTH // COLS
FPS = 60

# 顏色設定
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# 初始化畫面
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("逃離迷宮")
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
def draw_maze(maze, player_pos, goal_pos):
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

# 主程式
def main():
    maze = generate_maze(ROWS, COLS)
    player_pos = [0, 0]
    goal_pos = [COLS - 1, ROWS - 1]
    running = True

    while running:
        screen.fill(BLACK)
        draw_maze(maze, player_pos, goal_pos)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # 移動玩家
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:  # 上
            new_pos = [player_pos[0], player_pos[1] - 1]
        elif keys[pygame.K_s]:  # 下
            new_pos = [player_pos[0], player_pos[1] + 1]
        elif keys[pygame.K_a]:  # 左
            new_pos = [player_pos[0] - 1, player_pos[1]]
        elif keys[pygame.K_d]:  # 右
            new_pos = [player_pos[0] + 1, player_pos[1]]
        else:
            new_pos = player_pos

        # 檢查是否能移動
        if 0 <= new_pos[0] < COLS and 0 <= new_pos[1] < ROWS:
            if maze[new_pos[1]][new_pos[0]] == 0:
                player_pos = new_pos

        # 檢測勝利
        if player_pos == goal_pos:
            print("恭喜你逃出迷宮！")
            running = False

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
