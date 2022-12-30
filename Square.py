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

        self.lastDir = (0,0)
    
    def double(self) -> None:
        self.num *= 2

    def setNum(self, num: int) -> None:
        """Set a value to the square"""
        self.num = num
    
    def setIdx(self, idx: tuple[int, int]) -> None:
        """Set the square to a new index in the list"""
        self.idx = idx

    def getNum(self) -> int:
        """Get the number of square"""
        return self.num
    
    def getIdx(self) -> tuple[int, int]:
        """Get the indices of the square in the list"""
        return self.idx