class Solution:
    def judgeSquareSum(self, c: int) -> bool:  
        val = math.floor(math.sqrt(c))
        for a in range(0, val+1):
            b = math.sqrt(c - a**2)
            if b == int(b):
                return True
            
        return False 