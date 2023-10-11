class MyHashMap:
    def __init__(self):
        self.dic = [-1] * (10**6 + 1)
        
    def put(self, key: int, value: int) -> None:
        self.dic[key] = value

    def get(self, key: int) -> int:
        return self.dic[key]
        
    def remove(self, key: int) -> None:
        self.dic[key] = -1