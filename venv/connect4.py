import pygame

BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
WINDOW_WIDTH = 700
WINDOW_HEIGHT = 600
COLUMNS = 7
ROWS = 6
CELL_WIDTH = WINDOW_WIDTH / COLUMNS
CELL_HEIGHT = WINDOW_HEIGHT / ROWS

pygame.init()
size = (WINDOW_WIDTH, WINDOW_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Connect 4")
screen.fill(BLACK)

def drawGrid():
    for x in range(WINDOW_WIDTH):
        for y in range(WINDOW_HEIGHT):
            rect = pygame.Rect(x*CELL_WIDTH, y*CELL_HEIGHT,
                               CELL_WIDTH, CELL_HEIGHT)
            pygame.draw.rect(screen, BLUE, rect, 1)


while True:
    drawGrid()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    pygame.display.flip()
