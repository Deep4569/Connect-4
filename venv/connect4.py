import pygame
import math

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

size = (WINDOW_WIDTH, WINDOW_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Connect 4")

board = [[0] * COLUMNS for _ in range(ROWS)]

def drawGrid(board, game_started):
    for col in range(COLUMNS):
        for row in range(ROWS):
            pygame.draw.rect(screen, BLUE, (col * CELL_SIZE, row * CELL_SIZE + CELL_SIZE, CELL_SIZE, CELL_SIZE))
            pygame.draw.circle(screen, BLACK, (int(col * CELL_SIZE + CELL_SIZE / 2), int(row * CELL_SIZE + CELL_SIZE + CELL_SIZE / 2)), RADIUS)

    if game_started:
        for col in range(COLUMNS):
            for row in range(ROWS):
                color = RED if board[row][col] == 1 else (YELLOW if board[row][col] == 2 else BLACK)
                pygame.draw.circle(screen, color, (int(col * CELL_SIZE + CELL_SIZE / 2), WINDOW_HEIGHT - int(row * CELL_SIZE + CELL_SIZE / 2)), RADIUS)

def place_token(board, col, player):
    if board[ROWS-1][col] == 0:
        for row in range(ROWS):
            if board[row][col] == 0:
                board[row][col] = player
                break

def check_winning_move(board, player):
    directions = [ [1,0], [1,-1], [1,1], [0,1] ]
    for direction in directions:
        dirx = direction[0]
        diry = direction[1]

        for col in range(COLUMNS):
            for row in range(ROWS):
                lastx = row + 3*dirx
                lasty = col + 3*diry
                if (0 <= lastx and lastx < COLUMNS and 0 <= lasty and lasty < ROWS):
                    val = board[row][col];
                    if (val is not 0 and val == board[row+dirx][col+diry]
                                     and val == board[row+2 * dirx][col+2 * diry]
                                     and val == board[lastx][lasty]): return True
    return False

pygame.init()
player = 0
drawGrid(board, False)
game_finished = False

while not game_finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0, 0, WINDOW_WIDTH, CELL_SIZE))
            posx = event.pos[0]
            if player == 0:
                pygame.draw.circle(screen, RED, (posx, int(CELL_SIZE / 2)), RADIUS)
            else:
                pygame.draw.circle(screen, YELLOW, (posx, int(CELL_SIZE / 2)), RADIUS)
        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            posx = event.pos[0]
            col = int(math.floor(posx/CELL_SIZE))
            place_token(board, col, player+1)
            drawGrid(board,True)
            if check_winning_move(board, player+1):
                print("PLAYER %s WINS" % str(player+1))
                game_finished = True

            player = (player + 1) % 2