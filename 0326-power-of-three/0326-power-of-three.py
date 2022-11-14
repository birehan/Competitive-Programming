class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0: return False
        val = math.log(n, 3)
        return abs(val-round(val)) < 0.00000000001
        