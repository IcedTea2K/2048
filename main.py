import sys
import pygame as pg

def main():
    pg.init()
    SIZE = width, height = 500, 800
    SCREEN = pg.display.set_mode(SIZE)
    BGCOLOR = 250,248,239
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
        
        SCREEN.fill(BGCOLOR) # reset screen
        pg.display.flip()


if __name__ == '__main__':
    main()

