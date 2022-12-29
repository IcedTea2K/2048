class  Square:
    def __init__(self,num: int, idx: tuple[int, int], pos: tuple[int, int]) -> None:
        """Create a square with specified attributes
        num -- the number it currently holds
        idx -- tuple of its indices in the list
        pos -- position of the square
        """
        self.num = num
        self.idx = idx
        self.pos = pos
    
    def setNum(self, num: int) -> None:
        """Set a value to the square"""
        self.num = num
    
    def setIdx(self, idx: tuple[int, int]) -> None:
        """Set the square to a new index in the list"""
        self.idx = idx

    def setPos(self, newPos: tuple[int, int]) -> None:
        self.pos = newPos

    def getNum(self) -> int:
        """Get the number of square"""
        return self.num
    
    def getIdx(self) -> tuple[int, int]:
        """Get the indices of the square in the list"""
        return self.idx

    def getPos(self) -> tuple[int, int]:
        """get the position of the square on screen""" 
        return self.pos