class RandomizedSet:
    def __init__(self):
        self.store = set()
        
    def insert(self, val: int) -> bool:
        if val in self.store:
            return False
        
        self.store.add(val)
        return True 

    def remove(self, val: int) -> bool:
        if val not in self.store:
            return False
        
        self.store.remove(val)
        return True

    def getRandom(self) -> int:
        return random.choice(tuple(self.store))