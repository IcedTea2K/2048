import sys
import pygame as pg
import random
from Square import *

#################### Graphics ####################
SIZE = WIDTH, HEIGHT = 550, 800
SCREEN = pg.display.set_mode(SIZE)
BGCOLOR = 250,248,239

GRID_BGCOLOR = 187,173,160
GRID_SIZE = 500, 500
GRID_POS = (WIDTH /2, HEIGHT - GRID_SIZE[0]/2 - 30)
GRID_RECT = pg.Rect((0, 0), GRID_SIZE)
GRID_RECT.center = GRID_POS

SCORE_BOX_SIZE = 100, 40
SCORE_BOX_SURF = pg.Surface(SCORE_BOX_SIZE)
SCORE_BOX_SURF.fill((185, 173, 161))
HIGH_SCORE_BOX_RECT = pg.Rect((430, 70), SCORE_BOX_SIZE)
CURR_SCORE_BOX_RECT = pg.Rect((430 - SCORE_BOX_SIZE[0] - 4, 70), SCORE_BOX_SIZE)
SCORE_TXT_SIZE = 30

NEW_GAME_SIZE = 120, 40
NEW_GAME_SURF = pg.Surface(NEW_GAME_SIZE)
NEW_GAME_SURF.fill((140, 123, 104))
NEW_GAME_RECT = pg.Rect((427-60, 140), NEW_GAME_SIZE)
NEW_GAME_TXT_SIZE = 30

GAMEOVER_BGCOLOR = 156, 143, 132, 150
GAMEOVER_SURF = pg.Surface(GRID_SIZE, pg.SRCALPHA)
GAMEOVER_SURF.fill(GAMEOVER_BGCOLOR)
GAMEOVER_TXT_SIZE = 100

TITLE_TXT_SIZE = 100

#################### CELLS & SQUARES SPECS ####################
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


#################### Functions for Graphics ####################
def drawTitle() -> None:
    titleWriter = pg.font.Font(None, TITLE_TXT_SIZE)
    titleSurf = titleWriter.render('2048', True,(117, 110, 102))
    titleRect = titleSurf.get_rect(center=(150, 120))
    SCREEN.blit(titleSurf, titleRect)

def drawScoreBox() -> None:
    writer = pg.font.Font(None, SCORE_TXT_SIZE)
    currScoreTxtSurf = writer.render(str(currScore), True, (255, 255, 255))
    currScoreTxtRect = currScoreTxtSurf.get_rect(center=CURR_SCORE_BOX_RECT.center)

    highScoreTxtSurf = writer.render(str(highScore), True, (255, 255, 255))
    highScoreTxtRect = highScoreTxtSurf.get_rect(center=HIGH_SCORE_BOX_RECT.center)

    currScoreLableSurf = writer.render('Score', True, (119, 110, 101))
    currScoreLableRect = currScoreLableSurf.get_rect(center=(currScoreTxtRect.centerx, currScoreTxtRect.centery - 30))

    highScoreLableSurf = writer.render('Best', True, (119, 110, 101))
    highScoreLableRect = highScoreLableSurf.get_rect(center=(highScoreTxtRect.centerx, highScoreTxtRect.centery - 30))

    SCREEN.blit(SCORE_BOX_SURF, HIGH_SCORE_BOX_RECT)
    SCREEN.blit(highScoreTxtSurf, highScoreTxtRect)

    SCREEN.blit(SCORE_BOX_SURF, CURR_SCORE_BOX_RECT)
    SCREEN.blit(currScoreTxtSurf, currScoreTxtRect)

    SCREEN.blit(currScoreLableSurf, currScoreLableRect)
    SCREEN.blit(highScoreLableSurf, highScoreLableRect)

def drawButton():
    writer = pg.font.Font(None, NEW_GAME_TXT_SIZE)
    newGameTxtSurf = writer.render('New Game', True, (255, 255, 255))
    newGameTxtRect = newGameTxtSurf.get_rect(center=NEW_GAME_RECT.center)

    SCREEN.blit(NEW_GAME_SURF, NEW_GAME_RECT)
    SCREEN.blit(newGameTxtSurf, newGameTxtRect)

def drawCells(surface:pg.Surface, rects: list[list[pg.Rect]]) -> None:
    """Draw the (background) cells of the grid"""
    for x in rects:
        for y in x:
            SCREEN.blit(surface, y)

def renderSquares() -> None:
    smallWriter = pg.font.Font(None, SQUARE_TXT_SIZE_SMALL_NUM)
    largeWriter = pg.font.Font(None, SQUARE_TXT_SIZE_LARGE_NUM)
    for s in allSquares:
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

def gameOver() -> None:
    writer = pg.font.Font(None, GAMEOVER_TXT_SIZE)
    gameOverTxtSurf = writer.render('Game Over', True, (255, 255, 255))
    gameOverTxtRect = gameOverTxtSurf.get_rect(center=GRID_RECT.center)

    
    SCREEN.blit(GAMEOVER_SURF, GRID_RECT)
    SCREEN.blit(gameOverTxtSurf, gameOverTxtRect)

#################### Functions for Game Logic ####################
def isGameOver() -> bool:
    for y in range(4):
        for x in range(4):
            if (occupiedCells.get(((x+1), y)) is not None and \
                occupiedCells[(x+1, y)].getNum() == occupiedCells[(x, y)].getNum()) or \
                    (occupiedCells.get((x, y+1)) is not None and \
                        occupiedCells[(x, y+1)].getNum() == occupiedCells[(x, y)].getNum()):
                return False
    return True

def moveSquares(dir:tuple[int, int]) -> bool:
    container = [[] for i in range(4)]
    if dir == (1,0) or dir == (-1,0): # horizontally
        for s in allSquares:
            container[s.getIdx()[1]].append(s)
        container = [sorted(c, key=lambda s: s.getIdx()[0] * -dir[0]) for c in container] # sort to see which one is at front
    else: # moving vertically
        for s in allSquares:
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
                if occupiedCells.get((currX + dir[0], currY + dir[1])) is None:
                    currX += dir[0]
                    currY += dir[1]
                    hasMoved = True
                else:
                    hasMoved = combineSquare(s, occupiedCells.get((currX + dir[0], currY + dir[1]))) or hasMoved
                    break
            del occupiedCells[s.getIdx()]
            if s.getStatus():
                occupiedCells[(currX, currY)] = s
                s.setIdx((currX, currY))
                s.destRect = CELL_RECTS[currY][currX].copy()
            else:
                s.destRect = CELL_RECTS[currY + dir[1]][currX + dir[0]].copy()
            # print(occupiedCells)
    return hasMoved

def combineSquare(squareOne: Square, squareTwo: Square) -> bool:
    global currScore
    if squareOne.getNum() == squareTwo.getNum() and squareTwo.isCombining is False:
        squareOne.disable()
        squareTwo.double()
        currScore += squareTwo.getNum()
        squareTwo.isCombining = True
        squareOne.linkedSquare = squareTwo
        return True
    return False

def spawnSquare() -> None:
    potential = []
    for y in range(4):
        for x in range(4):
            if occupiedCells.get((x,y)) is None:
                potential.append((x,y))
    if len(potential) == 0:
        return
    idx = random.choice(potential)
    allSquares.append(Square(random.choice([2,2,2,2,2,2,4]), idx, CELL_RECTS[idx[1]][idx[0]].copy()))
    occupiedCells[idx] = allSquares[-1]

def updateSquares(hasMoved: bool) -> bool:
    noneIsMoving = True
    for s in allSquares:
        s.update()
        if s.getStatus() == False and s.isMoving == False:
            s.linkedSquare.isCombining = False
            s.linkedSquare.isInflating = True
            allSquares.remove(s)
        elif s.isMoving:
            noneIsMoving = False
    if noneIsMoving and hasMoved:
        spawnSquare()
        return False
    return hasMoved
    
def main():
    # initialize the game
    pg.init()
    pg.font.init()
    
    global allSquares
    global occupiedCells
    allSquares = []
    occupiedCells = {}
    spawnSquare() 
    spawnSquare()  
    hasMoved = False

    global highScore
    global currScore
    highScore = 0
    currScore = 0
    with open('high_score.txt', 'a+') as f: # get local high score
        f.seek(0)
        m = f.read()
        if m != '':
            highScore = int(m)
        else:
            highScore = 0

    # main game loop
    while True:
        if currScore > highScore:
            highScore = currScore
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                with open('high_score.txt', 'w') as f:
                    f.write(str(highScore)) 
                sys.exit()
            elif event.type == pg.KEYUP:
                if event.key == pg.K_UP:
                    hasMoved = moveSquares((0,-1))
                elif event.key == pg.K_RIGHT:
                    hasMoved = moveSquares((1, 0))
                elif event.key == pg.K_LEFT:
                    hasMoved = moveSquares((-1, 0))
                elif event.key == pg.K_DOWN:
                    hasMoved = moveSquares((0, 1))
            elif event.type == pg.MOUSEBUTTONDOWN:
                if NEW_GAME_RECT.collidepoint(pg.mouse.get_pos()):
                    allSquares = []
                    occupiedCells = {}
                    spawnSquare() 
                    spawnSquare()
                    currScore = 0
        # Draw background
        SCREEN.fill(BGCOLOR) # reset screen
        pg.draw.rect(SCREEN, GRID_BGCOLOR, GRID_RECT) # draw grid background
        drawCells(CELL_SURFACE, CELL_RECTS) # draw each cells of grid
        hasMoved = updateSquares(hasMoved)
        drawScoreBox()
        drawButton()
        drawTitle()
        
        # draw squares
        renderSquares()
        if len(occupiedCells) == 16 and isGameOver():
            gameOver()
        pg.display.flip()

if __name__ == '__main__':
    main()
