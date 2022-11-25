class MedianFinder:

    def __init__(self):
        self.array = []

    def addNum(self, num: int) -> None:
        index = bisect_left(self.array, num)
        self.array.insert(index, num)
        

    def findMedian(self) -> float:
        length = len(self.array)
        if length % 2 == 0:
            return (self.array[length//2] + self.array[(length//2)-1])/2
        else:
            return self.array[length//2]
            
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()