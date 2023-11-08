class AllOne:

    def __init__(self):
        self.store = defaultdict(int)
        self.max_heap = [ ]
        self.min_heap = [ ]


    def inc(self, key: str) -> None:
        self.store[key] += 1
        heappush(self.max_heap, (-self.store[key], key))
        heappush(self.min_heap, (self.store[key], key))


    def dec(self, key: str) -> None:
        self.store[key] -= 1
        if self.store[key] == 0:
            del self.store[key]
        else:
            heappush(self.max_heap, (-self.store[key], key))
            heappush(self.min_heap, (self.store[key], key))
        

    def getMaxKey(self) -> str:
        while self.max_heap and abs(self.max_heap[0][0]) != self.store[self.max_heap[0][1]]:
            heappop(self.max_heap)
        
        if self.max_heap:
            return self.max_heap[0][1]

        return ""
    
    def getMinKey(self) -> str:
        while self.min_heap and abs(self.min_heap[0][0]) != self.store[self.min_heap[0][1]]:
            heappop(self.min_heap)
        
        if self.min_heap:
            return self.min_heap[0][1]

        return ""


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()