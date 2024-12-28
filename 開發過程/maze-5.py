import pygame
import random
import sys
import time

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 800  # Window size
GRID_SIZE = 25  # Grid size (25x25)
CELL_SIZE = WIDTH // GRID_SIZE  # Size of each cell
FPS = 60  # Frame rate

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Directions for maze generation and movement
DIRECTIONS = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # Up, Right, Down, Left

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mouse and Keyboard Maze Escape")

# Font
font = pygame.font.Font(None, 48)


def create_maze(grid_size):
    """Generates a maze using depth-first search."""
    maze = [[1] * grid_size for _ in range(grid_size)]  # 1 = wall, 0 = path
    stack = [(0, 0)]  # Start position
    maze[0][0] = 0  # Mark the start as a path

    while stack:
        x, y = stack[-1]
        neighbors = []
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx * 2, y + dy * 2
            if 0 <= nx < grid_size and 0 <= ny < grid_size and maze[nx][ny] == 1:
                neighbors.append((nx, ny, dx, dy))

        if neighbors:
            nx, ny, dx, dy = random.choice(neighbors)
            maze[x + dx][y + dy] = 0  # Remove wall
            maze[nx][ny] = 0  # Mark new cell as path
            stack.append((nx, ny))
        else:
            stack.pop()

    return maze


def draw_maze(maze):
    """Draws the maze on the screen."""
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            color = WHITE if maze[x][y] == 1 else BLACK
            pygame.draw.rect(screen, color, (y * CELL_SIZE, x * CELL_SIZE, CELL_SIZE, CELL_SIZE))


def draw_player(x, y):
    """Draws the player on the screen."""
    pygame.draw.rect(screen, BLUE, (y * CELL_SIZE, x * CELL_SIZE, CELL_SIZE, CELL_SIZE))


def draw_end(x, y):
    """Draws the goal on the screen."""
    pygame.draw.rect(screen, GREEN, (y * CELL_SIZE, x * CELL_SIZE, CELL_SIZE, CELL_SIZE))


def display_win_message(time_taken, steps):
    """Displays the win message."""
    screen.fill(WHITE)
    win_text = f"You Win! Time: {time_taken:.1f} seconds, Steps: {steps}"
    text_surface = font.render(win_text, True, GREEN)
    screen.blit(text_surface, (WIDTH // 2 - text_surface.get_width() // 2, HEIGHT // 2 - text_surface.get_height() // 2))
    pygame.display.update()
    time.sleep(3)


def main():
    # Create maze
    maze = create_maze(GRID_SIZE)
    player_x, player_y = 0, 0  # Starting position
    end_x, end_y = GRID_SIZE - 1, GRID_SIZE - 1  # End position

    # Game variables
    clock = pygame.time.Clock()
    start_time = time.time()
    steps = 0

    running = True
    while running:
        screen.fill(BLACK)
        draw_maze(maze)
        draw_player(player_x, player_y)
        draw_end(end_x, end_y)

        pygame.display.update()
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:  # Move up
                    new_x, new_y = player_x - 1, player_y
                elif event.key == pygame.K_s:  # Move down
                    new_x, new_y = player_x + 1, player_y
                elif event.key == pygame.K_a:  # Move left
                    new_x, new_y = player_x, player_y - 1
                elif event.key == pygame.K_d:  # Move right
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
            display_win_message(time_taken, steps)
            running = False


if __name__ == "__main__":
    main()
