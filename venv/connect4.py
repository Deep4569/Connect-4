import pygame
import math
import sys

BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
COLUMNS = 7
ROWS = 6
CELL_SIZE = 100
WINDOW_WIDTH = COLUMNS * CELL_SIZE
WINDOW_HEIGHT = (ROWS+1) * CELL_SIZE
RADIUS = int(CELL_SIZE/2 - 5)

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Connect 4")

board = [[None] * COLUMNS for _ in range(ROWS)]

def drawGrid(board, game_started):
    for col in range(COLUMNS):
        for row in range(ROWS):
            width = col * CELL_SIZE
            height = row * CELL_SIZE + CELL_SIZE
            pygame.draw.rect(screen, BLUE, (width, height, CELL_SIZE, CELL_SIZE))
            pygame.draw.circle(screen, BLACK, (int(width + CELL_SIZE / 2), int(height + CELL_SIZE / 2)), RADIUS)

    if game_started:
        for col in range(COLUMNS):
            for row in range(ROWS):
                color = RED if board[row][col] == 0 else (YELLOW if board[row][col] == 1 else BLACK)
                pygame.draw.circle(screen, color, (int(col * CELL_SIZE + CELL_SIZE / 2), WINDOW_HEIGHT - int(row * CELL_SIZE + CELL_SIZE / 2)), RADIUS)

def place_token(board, col, player):
    if board[ROWS-1][col]is None:
        for row in range(ROWS):
            if board[row][col] is None:
                board[row][col] = player
                break

def check_winning_move(board, player):
    directions = [[1,0], [1,-1], [1,1], [0,1]]
    for direction in directions:
        dirx = direction[0]
        diry = direction[1]

        for col in range(COLUMNS):
            for row in range(ROWS):
                lastx = row + 3*dirx
                lasty = col + 3*diry
                if (0 <= lastx and lastx < COLUMNS and 0 <= lasty and lasty < ROWS):
                    val = board[row][col];
                    if (val is not None and val == board[row+dirx][col+diry]
                                     and val == board[row+2 * dirx][col+2 * diry]
                                     and val == board[lastx][lasty]): return True
    return False


player = 0
drawGrid(board, False)
game_finished = False

while not game_finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0, 0, WINDOW_WIDTH, CELL_SIZE))
            posx = event.pos[0]
            color = RED if player == 0 else YELLOW
            pygame.draw.circle(screen, color, (posx, int(CELL_SIZE / 2)), RADIUS)
        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            posx = event.pos[0]
            col = int(math.floor(posx/CELL_SIZE))
            place_token(board, col, player)
            drawGrid(board,True)
            if check_winning_move(board, player):
                print("PLAYER %i WINS" % (player+1))
                game_finished = True

            player = (player + 1) % 2