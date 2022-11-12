class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        val = pow(2,p) - 1
        mod = pow(10, 9) + 7
        res = pow(val-1, val//2, mod)
        return (val * res) % (pow(10, 9) + 7)