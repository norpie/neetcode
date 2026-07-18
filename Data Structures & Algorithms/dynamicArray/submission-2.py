class DynamicArray:

    content: []
    size: int
    capacity: int
    
    def __init__(self, capacity: int):
        self.content = []
        self.size = 0
        self.capacity = capacity


    def get(self, i: int) -> int:
        return self.content[i]


    def set(self, i: int, n: int) -> None:
        self.content[i] = n


    def pushback(self, n: int) -> None:
        if len(self.content) == self.capacity:
            self.resize()
        self.content.append(n)
        self.size += 1


    def popback(self) -> int:
        rv = self.content.pop(self.size - 1)
        self.size -= 1
        return rv
 

    def resize(self) -> None:
        self.capacity = self.capacity * 2


    def getSize(self) -> int:
        return self.size
        
    
    def getCapacity(self) -> int:
        return self.capacity
