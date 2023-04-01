class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        start = -1
        while n:
            if (n & 1 and start == 1) or (not (n & 1) and start == 0):
                return False
            start = (n & 1) 
            n >>= 1
        
        return True