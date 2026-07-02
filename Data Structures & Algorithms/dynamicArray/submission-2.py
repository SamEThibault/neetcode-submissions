class DynamicArray:

    def __init__(self, capacity: int):
        self.arr = [None] * capacity
        self.capacity = capacity
        self.size = 0

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.size >= self.capacity:
            self.resize()
        
        self.arr[self.size] = n
        self.size += 1

    def popback(self) -> int:
        element = self.arr[self.size - 1]
        self.arr[-1] = None
        self.size -= 1
        return element

    def resize(self) -> None:
        self.arr = self.arr + [None] * self.capacity
        self.capacity = self.capacity * 2

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity