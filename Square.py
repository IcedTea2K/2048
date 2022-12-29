import pygame as pg
class  Square:
    def __init__(self,num: int, idx: tuple[int, int], rect: pg.rect.Rect) -> None:
        """Create a square with specified attributes
        num -- the number it currently holds
        idx -- tuple of its indices in the list
        rect -- position (and size) of the square
        """
        self.num = num
        self.idx = idx
        self.rect = rect

        self.lastMovement = (0,0)
        self.isMoving = False
    
    def setNum(self, num: int) -> None:
        """Set a value to the square"""
        self.num = num
    
    def setIdx(self, idx: tuple[int, int]) -> None:
        """Set the square to a new index in the list"""
        self.idx = idx

    def moveSquare(self, dist=None) -> None:
        if dist is None:
            self.rect = self.rect.move(self.lastMovement)
        else:
            self.rect = self.rect.move(dist)
            self.lastMovement = dist
            self.isMoving = True

    def getNum(self) -> int:
        """Get the number of square"""
        return self.num
    
    def getIdx(self) -> tuple[int, int]:
        """Get the indices of the square in the list"""
        return self.idx

    def getRect(self) -> pg.rect.Rect:
        """get the position of the square on screen""" 
        return self.rect