class  Square:
    def __init__(self, idx: tuple[int, int], num=None, isActive=False) -> None:
        """Create a square with specified attributes
        num -- the number it currently holds
        idx -- tuple of its indices in the list
        isActive -- status of the square; active square will be rendered
        """
        self.num = num
        self.idx = idx
        self.isActive = False
    
    def activateSquare(self, num: int) -> None:
        """Activate the square with specified value"""
        self.isActive = True
        self.num = num
    
    def deactivateSquare(self) -> None:
        """Deactivate the square"""
        self.isActive = False

    def setNum(self, num: int) -> None:
        """Set a value to the square"""
        self.num = num
    
    def setIdx(self, idx: tuple[int, int]) -> None:
        """Set the square to a new index in the list"""
        self.idx = idx

    def getStatus(self) -> bool:
        """Get the status of the square"""
        return self.isActive

    def getNum(self) -> int:
        """Get the number of square"""
        return self.num
    
    def getIdx(self) -> tuple[int, int]:
        """Get the indices of the square in the list"""
        return self.idx