import random
class RandomizedSet:
    
    def __init__(self):
        self.list = []
        self.index_map = dict()

    def insert(self, val: int) -> bool:
        if val in self.index_map:
            return False
        self.list.append(val)
        self.index_map[val]=len(self.list)-1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.list:
            return False
        idx = self.index_map[val]
        last_element = self.list[len(self.list)-1]
        self.list[idx], self.list[len(self.list)-1] = self.list[len(self.list)-1], self.list[idx]
        self.list.pop()
        self.index_map[last_element]=idx
        del self.index_map[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()