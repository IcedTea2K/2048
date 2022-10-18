import sys
import pygame as pg

def main():
    pg.init()
    size = width, height = 300, 300
    screen = pg.display.set_mode(size)
    black = 255,255,255
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
        
        screen.fill(black) # reset screen
        pg.display.flip()


if __name__ == '__main__':
    main()

