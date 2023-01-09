class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.valid = 0
        

    def consec(self, num: int) -> bool:
        if num == self.value: self.valid += 1
        else: self.valid = 0

        return self.valid >= self.k