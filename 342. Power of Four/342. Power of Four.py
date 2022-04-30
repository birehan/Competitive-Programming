class Solution:
    def isPowerOfFour(self, n: int) -> bool:

        def helper(n):
            if n == 0 or n % 4 != 0:
                return n

            else:
                return helper(n // 4)

        if helper(n) == 1:
            return True

        return False

