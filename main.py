import sys
import pygame as pg

def main():
    pg.init()
    SIZE = WIDTH, HEIGHT = 550, 800
    SCREEN = pg.display.set_mode(SIZE)
    BGCOLOR = 250,248,239

    GRID_BGCOLOR = 187,173,160
    GRID_SIZE = 500, 500
    GRID_POS = (WIDTH /2, HEIGHT - GRID_SIZE[0]/2 - 30)
    GRID_RECT = pg.Rect((0, 0), GRID_SIZE)
    GRID_RECT.center = GRID_POS

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
        
        SCREEN.fill(BGCOLOR) # reset screen
        pg.draw.rect(SCREEN, GRID_BGCOLOR, GRID_RECT)
        pg.display.flip()


if __name__ == '__main__':
    main()

