import sys
import pygame as pg
import random
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
    for x in range(0,4)] for y in range(0,4)]
CELL_SURFACE = pg.Surface(CELL_SIZE, pg.SRCALPHA) 
CELL_SURFACE.fill(CELL_COLOR) # set color of the cell

SQUARE_SPEED = 6
SQUARE_COLOR = {2: (234, 228, 220), 4: (234, 226, 210),\
    8: (225, 182, 139), 16: (222, 158, 122), 32: (218, 137, 115),\
        64: (214, 114, 89), 128:(231, 215, 159), 256: (229, 213, 150),\
            512: (235, 214, 127), 1024: (228, 208, 132), 2048: (224, 198, 90),\
                4096: (61, 59, 53), 8192: (59, 58, 52)}
SQUARE_SURFACE = pg.Surface(CELL_SIZE)
SQUARE_TXT_SIZE_SMALL_NUM = 80
SQUARE_TXT_SIZE_LARGE_NUM = 50
SQUARE_TXT_COLOR_SMALL_NUM = (119, 110, 101)
SQUARE_TXT_COLOR_LARGE_NUM = (255, 255, 255)

def main():
    pg.init()
    pg.font.init()
    smallWriter = pg.font.Font(None, SQUARE_TXT_SIZE_SMALL_NUM)
    largeWrite = pg.font.Font(None, SQUARE_TXT_SIZE_LARGE_NUM)
    # allSquares = [Square(8, (0,0), CELL_RECTS[0][0].copy()), Square(8, (1,0), CELL_RECTS[0][1].copy()),\
    #     Square(4, (0,1), CELL_RECTS[1][0].copy()), Square(2, (1,1), CELL_RECTS[1][1].copy()), Square(8, (2,0), CELL_RECTS[0][2].copy())] # list of all the squares in the game
    # occupiedCells = {(0,0): allSquares[0], (1,0): allSquares[1],\
    #     (0,1): allSquares[2], (1,1):allSquares[3], (2,0):allSquares[4]}
    allSquares = []
    occupiedCells = {}
    spawnSquare(allSquares, occupiedCells) 
    spawnSquare(allSquares, occupiedCells)  
    hasMoved = False
    while True:
        frameCount = int(((pg.time.get_ticks() / 1000) * 60)%60)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.KEYUP:
                if event.key == pg.K_UP:
                    hasMoved = moveSquares(allSquares, (0,-1), occupiedCells)
                elif event.key == pg.K_RIGHT:
                    hasMoved = moveSquares(allSquares, (1, 0), occupiedCells)
                elif event.key == pg.K_LEFT:
                    hasMoved = moveSquares(allSquares, (-1, 0), occupiedCells)
                elif event.key == pg.K_DOWN:
                    hasMoved = moveSquares(allSquares, (0, 1), occupiedCells)
        SCREEN.fill(BGCOLOR) # reset screen
        pg.draw.rect(SCREEN, GRID_BGCOLOR, GRID_RECT) # draw grid background
        drawCells(CELL_SURFACE, CELL_RECTS) # draw each cells of grid
        hasMoved = updateSquares(allSquares, occupiedCells, frameCount, hasMoved)
        renderSquares(smallWriter, largeWrite, allSquares)
        pg.display.flip()

def moveSquares(squares: list[Square], dir:tuple[int, int], occupied: dict[tuple[int, int]: Square]) -> bool:
    container = [[] for i in range(4)]
    if dir == (1,0) or dir == (-1,0): # horizontally
        for s in squares:
            container[s.getIdx()[1]].append(s)
        container = [sorted(c, key=lambda s: s.getIdx()[0] * -dir[0]) for c in container] # sort to see which one is at front
    else: # moving vertically
        for s in squares:
            container[s.getIdx()[0]].append(s) 
        container = [sorted(c, key=lambda s: s.getIdx()[1] * -dir[1]) for c in container]
    hasMoved = False
    for c in container:
        for s in c:
            if s.getStatus() == False:
                continue
            currX = s.getIdx()[0]
            currY = s.getIdx()[1] 
            while currX + dir[0] < 4 and currY + dir[1] < 4 and\
                currX + dir[0] >= 0 and currY + dir[1] >= 0:
                if occupied.get((currX + dir[0], currY + dir[1])) is None:
                    currX += dir[0]
                    currY += dir[1]
                    hasMoved = True
                else:
                    hasMoved = combineSquare(s, occupied.get((currX + dir[0], currY + dir[1]))) or hasMoved
                    break
            del occupied[s.getIdx()]
            if s.getStatus():
                occupied[(currX, currY)] = s
                s.setIdx((currX, currY))
                s.destRect = CELL_RECTS[currY][currX].copy()
            else:
                s.destRect = CELL_RECTS[currY + dir[1]][currX + dir[0]].copy()
            # print(occupied)
    return hasMoved

def combineSquare(squareOne: Square, squareTwo: Square) -> bool:
    if squareOne.getNum() == squareTwo.getNum() and squareTwo.isCombining is False:
        squareOne.disable()
        squareTwo.double()
        squareTwo.isCombining = True
        squareOne.linkedSquare = squareTwo
        return True
    return False

def spawnSquare(squares: list[Square], occupied: dict[tuple[int, int]: Square]) -> None:
    potential = []
    for y in range(4):
        for x in range(4):
            if occupied.get((x,y)) is None:
                potential.append((x,y))
    if len(potential) == 0:
        return
    idx = random.choice(potential)
    squares.append(Square(random.choice([2,2,2,2,2,2,4]), idx, CELL_RECTS[idx[1]][idx[0]].copy()))
    occupied[idx] = squares[-1]

def updateSquares(los: list[Square], occupied: dict[tuple[int, int]: Square], frameCount: int, hasMoved: bool) -> bool:
    noneIsMoving = True
    for s in los:
        s.update(frameCount)
        if s.getStatus() == False and s.isMoving == False:
            s.linkedSquare.isCombining = False
            s.linkedSquare.isInflating = True
            los.remove(s)
        elif s.isMoving:
            noneIsMoving = False
    if noneIsMoving and hasMoved:
        spawnSquare(los, occupied)
        return False
    return hasMoved
    

def renderSquares(smallWriter: pg.font, largeWriter: pg.font, los: list[Square]) -> None:
    for s in los:
        squareVal = s.getNum() if s.isCombining is False else int(s.getNum()/2)
        textSurf = None
        if squareVal <= 4:
            textSurf = smallWriter.render(str(squareVal), True, SQUARE_TXT_COLOR_SMALL_NUM)
        elif squareVal < 1000:
            textSurf = smallWriter.render(str(squareVal), True, SQUARE_TXT_COLOR_LARGE_NUM)
        else:
            textSurf = largeWriter.render(str(squareVal), True, SQUARE_TXT_COLOR_LARGE_NUM)

        textRect = textSurf.get_rect(center=s.currRect.center)
        SQUARE_SURFACE.fill(SQUARE_COLOR.get(squareVal))
        SCREEN.blit(pg.transform.scale(SQUARE_SURFACE, s.currRect.size), s.currRect)
        SCREEN.blit(textSurf, textRect)
         

def drawCells(surface:pg.Surface, rects: list[list[pg.Rect]]) -> None:
    """Draw the (background) cells of the grid"""
    for x in rects:
        for y in x:
            SCREEN.blit(surface, y)

if __name__ == '__main__':
    main()
