from typing import List

class LinkedList:

    content: List
    size = int
    
    def __init__(self):
        self.content = []
        self.size = 0

    
    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        return self.content[index]

    def insertHead(self, val: int) -> None:
        self.content.insert(0, val)
        self.size += 1
        

    def insertTail(self, val: int) -> None:
        self.content.append(val)
        self.size += 1

    def remove(self, index: int) -> bool:
        if index >= self.size:
            return False
        self.size -= 1
        self.content.pop(index)
        return True

    def getValues(self) -> List[int]:
        return self.content
        
