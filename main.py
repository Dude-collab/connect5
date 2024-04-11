import pygame
import sys

pygame.init()

# Constants
SCREEN_SIZE = 600
ROWS, COLS = 15, 15
SQUARE_SIZE = SCREEN_SIZE // COLS

# RGB Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
YELLOW = (255, 249, 196)
# Setup display
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption('Gomoku')

def draw_board():
    screen.fill(YELLOW)
    for row in range(ROWS):
        for col in range(COLS):
            rect = pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
            pygame.draw.rect(screen, GRAY, rect, 1)

def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_board()
        pygame.display.update()

    pygame.quit()
    sys.exit()

board = [[None for _ in range(COLS)] for _ in range(ROWS)]
current_player = BLACK  # Start with black

def place_stone(row, col):
    global current_player
    if board[row][col] is None:
        board[row][col] = current_player
        if check_win(row, col):
            print(f"{current_player} wins!")
            pygame.quit()
            sys.exit()
        current_player = WHITE if current_player == BLACK else BLACK

def check_win(row, col):
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
    for dr, dc in directions:
        count = 1
        for n in range(1, 5):  # Check forwards
            r, c = row + dr * n, col + dc * n
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or board[r][c] != board[row][col]:
                break
            count += 1
        for n in range(1, 5):  # Check backwards
            r, c = row - dr * n, col - dc * n
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or board[r][c] != board[row][col]:
                break
            count += 1
        if count >= 5:
            return True
    return False

def draw_stones():
    for row in range(ROWS):
        for col in range(COLS):
            stone = board[row][col]
            if stone:
                center = (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2)
                pygame.draw.circle(screen, stone, center, SQUARE_SIZE // 2 - 3)

def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                col, row = x // SQUARE_SIZE, y // SQUARE_SIZE
                place_stone(row, col)

        draw_board()
        draw_stones()
        pygame.display.update()

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()



