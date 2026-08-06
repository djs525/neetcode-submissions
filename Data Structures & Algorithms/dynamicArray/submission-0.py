class DynamicArray:
    
    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("capacity must be > 0")
        self.capacity = capacity
        self.size = 0
        self.array = [None] * capacity

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        self.array[self.size] = n
        self.size += 1
        

    def popback(self) -> int:
        end = self.size - 1
        end_element = self.array[end]  
        self.array[end] = None
        self.size -= 1
        return end_element
        

    def resize(self) -> None:
        new_cap = self.capacity * 2
        new_arr = [None] * new_cap

        for i in range(self.size):
            new_arr[i] = self.array[i]
        self.array = new_arr
        self.capacity = new_cap

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity
