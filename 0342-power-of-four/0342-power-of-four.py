class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0: return False
        val = math.log(n, 4)
        return abs(val - round(val)) < 0.00000001
