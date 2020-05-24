import pygame
import math

BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
COLUMNS = 7
ROWS = 6
SQUARESIZE = 100
WINDOW_WIDTH = COLUMNS * SQUARESIZE
WINDOW_HEIGHT = (ROWS+1) * SQUARESIZE
RADIUS = int(SQUARESIZE/2 - 5)

size = (WINDOW_WIDTH, WINDOW_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Connect 4")

board = [[0] * COLUMNS for _ in range(ROWS)]

def drawGrid(board, game_started):
    for col in range(COLUMNS):
        for row in range(ROWS):
            pygame.draw.rect(screen, BLUE, (col * SQUARESIZE, row * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, BLACK, (int(col * SQUARESIZE + SQUARESIZE / 2), int(row * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)), RADIUS)

    if game_started:
        for col in range(COLUMNS):
            for row in range(ROWS):
                color = RED if board[row][col] == 1 else (YELLOW if board[row][col] == 2 else BLACK)
                pygame.draw.circle(screen, color, (int(col * SQUARESIZE + SQUARESIZE / 2), WINDOW_HEIGHT - int(row * SQUARESIZE + SQUARESIZE / 2)), RADIUS)

def place_token(board, col, player):
    if board[ROWS-1][col] == 0:
        for row in range(ROWS):
            if board[row][col] == 0:
                board[row][col] = player
                break

pygame.init()
player = 0
drawGrid(board, False)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0, 0, WINDOW_WIDTH, SQUARESIZE))
            posx = event.pos[0]
            if player == 0:
                pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE / 2)), RADIUS)
            else:
                pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE / 2)), RADIUS)
        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            posx = event.pos[0]
            col = int(math.floor(posx/SQUARESIZE))
            place_token(board, col, player+1)
            drawGrid(board,True)

            player = (player + 1) % 2