import sys
import pygame as pg
from Square import *

SIZE = WIDTH, HEIGHT = 550, 800
SCREEN = pg.display.set_mode(SIZE)
BGCOLOR = 250,248,239

GRID_BGCOLOR = 187,173,160
GRID_SIZE = 500, 500
GRID_POS = (WIDTH /2, HEIGHT - GRID_SIZE[0]/2 - 30)
GRID_RECT = pg.Rect((0, 0), GRID_SIZE)
GRID_RECT.center = GRID_POS

CELL_SIZE = 106, 106
CELL_COLOR = 238,228,218,100
PADDING = (GRID_SIZE[0] - CELL_SIZE[0]*4)/5
CELL_RECTS = [[pg.Rect((x*CELL_SIZE[0] + PADDING*(x+1) + GRID_RECT.topleft[0], y*CELL_SIZE[1] + PADDING*(y+1) + GRID_RECT.topleft[1]), CELL_SIZE) \
    for y in range(0,4)] for x in range(0,4)]
CELL_SURFACE = pg.Surface(CELL_SIZE, pg.SRCALPHA) 
CELL_SURFACE.fill(CELL_COLOR) # set color of the cell

SQUARE_SPEED = 3
SQUARE_COLOR = 238, 228, 218
SQUARE_SURFACE = pg.Surface(CELL_SIZE)
SQUARE_SURFACE.fill(SQUARE_COLOR)
SQUARE_TXT_SIZE = 80
SQUARE_TXT_COLOR = 119, 110, 101

def main():
    pg.init()
    pg.font.init()
    writer = pg.font.Font(None, SQUARE_TXT_SIZE)
    allSquares = [Square(2, (0,0), CELL_RECTS[0][0])] # list of all the squares in the game
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
        
        SCREEN.fill(BGCOLOR) # reset screen
        pg.draw.rect(SCREEN, GRID_BGCOLOR, GRID_RECT) # draw grid background
        drawCells(CELL_SURFACE, CELL_RECTS) # draw each cells of grid
        renderSquare(writer, allSquares)
        pg.display.flip()

def moveSquare():
    pass

def combineSquare():
    pass

def spawnSquare():
    pass

def renderSquare(writer: pg.font, los: list[Square]):
    for s in los:
        textSurf = writer.render('2', True, SQUARE_TXT_COLOR)
        textRect = textSurf.get_rect(center = s.getRect().center)
        SCREEN.blit(SQUARE_SURFACE, s.getRect())
        SCREEN.blit(textSurf, textRect)
        # print('aa')
         

def drawCells(surface:pg.Surface, rects: list[list[pg.Rect]]) -> None:
    """Draw the (background) cells of the grid"""
    for x in rects:
        for y in x:
            SCREEN.blit(surface, y)

if __name__ == '__main__':
    main()
