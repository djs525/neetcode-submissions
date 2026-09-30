class RandomizedSet:

    def __init__(self):
        self.vals = []
        self.hashMap = {} #value : index

    def insert(self, val: int) -> bool:
        if val in self.hashMap:
            return False
        self.hashMap[val] = len(self.vals)
        self.vals.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.hashMap:
            return False
        
        i = self.hashMap[val] #index of val
        last = self.vals[-1] #last element
        
        self.hashMap[last] = i
        self.vals[i] = last #updating the removed position with the last element
        self.vals.pop() #removing the duplicate last element
        del self.hashMap[val]
        
        return True

    def getRandom(self) -> int:
        return random.choice(self.vals)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()