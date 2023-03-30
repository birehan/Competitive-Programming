class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        start = x ^ y
        count = 0
        
        while start > 0:
            count += start & 1
            start >>= 1
        
        return count