import pygame as pg
class  Square:
    SPEED = 80
    INFLATION_RATE = 4
    MAX_SIZE = (130, 130)
    ORG_SIZE = (106, 106)
    def __init__(self,num: int, idx: tuple[int, int], rect: pg.rect.Rect) -> None:
        """Create a square with specified attributes
        num -- the number it currently holds
        idx -- tuple of its indices in the list
        rect -- position (and size) of the square
        """
        self.num = num
        self.idx = idx
        self.currRect = rect
        self.destRect = self.currRect
        
        self.status = True
        self.isMoving = False
        self.isCombining = False
        self.linkedSquare = None
        self.isInflating = True
    
    def double(self) -> None:
        self.num *= 2

    def setNum(self, num: int) -> None:
        """Set a value to the square"""
        self.num = num
    
    def setIdx(self, idx: tuple[int, int]) -> None:
        """Set the square to a new index in the list"""
        if self.idx != idx:
            self.isMoving = True
            self.idx = idx

    def getNum(self) -> int:
        """Get the number of square"""
        return self.num
    
    def getIdx(self) -> tuple[int, int]:
        """Get the indices of the square in the list"""
        return self.idx
    
    def disable(self) -> None:
        self.status = False
    
    def getStatus(self) -> bool:
        return self.status

    def inflate(self) -> None:
        if self.isInflating:
            if self.currRect.size[0] + self.INFLATION_RATE < self.MAX_SIZE[0]:
                self.currRect = self.currRect.inflate(self.INFLATION_RATE, self.INFLATION_RATE)
            else:
                self.currRect.size = self.MAX_SIZE
                self.isInflating = False
        else:
            if self.currRect.size[0] - self.INFLATION_RATE > self.ORG_SIZE[0]:
                self.currRect.inflate_ip(-self.INFLATION_RATE, -self.INFLATION_RATE) 
            else:
                self.currRect.size = self.ORG_SIZE

    def update(self) -> None:
        if self.currRect.center == self.destRect.center:
            self.isMoving = False
            self.inflate()
            
            return
        self.isMoving = True 
        if self.currRect.centerx + self.SPEED <= self.destRect.centerx:
            self.currRect.move_ip(self.SPEED, 0)
        elif self.currRect.centerx - self.SPEED >= self.destRect.centerx:
            self.currRect.move_ip(-self.SPEED, 0)
        elif self.currRect.centery + self.SPEED <= self.destRect.centery:
            self.currRect.move_ip(0, self.SPEED)
        elif self.currRect.centery - self.SPEED >= self.destRect.centery:
            self.currRect.move_ip(0, -self.SPEED)
        else:
            self.currRect = self.destRect
