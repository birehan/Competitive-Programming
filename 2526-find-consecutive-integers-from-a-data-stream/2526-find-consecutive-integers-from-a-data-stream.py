class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.value_count = 0
      
    def consec(self, num: int) -> bool:
        if num == self.value: self.value_count += 1
        else: self.value_count = 0
            
        return self.value_count  >= self.k

       