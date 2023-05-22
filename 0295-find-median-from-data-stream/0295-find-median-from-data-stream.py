class MedianFinder:

    def __init__(self):
        self.heap1 = []
        self.heap2 = []

    def addNum(self, num: int) -> None:
        heappush(self.heap1, num)
        
        while len(self.heap1) - len(self.heap2) > 2:
            heappush(self.heap2, -heappop(self.heap1))
        
        if self.heap1 and self.heap2 and -self.heap2[0] > self.heap1[0]:
            a, b = heappop(self.heap1), heappop(self.heap2)
            heappush(self.heap1, -b)
            heappush(self.heap2, -a)


    def findMedian(self) -> float:
        if (len(self.heap1) + len(self.heap2)) % 2 == 1:
            return self.heap1[0]
        else:
            num1, num2 = heappop(self.heap1), heappop(self.heap1)
            heappush(self.heap1, num1)
            heappush(self.heap1, num2)

            return (num1 + num2)/2
        