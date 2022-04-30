class Solution:
    def fib(self, n: int) -> int:

        def helper(f0, f1, n):
            if n == 0:
                return 0
            if n == 1:
                return f1
            else:
                f2 = f0 + f1
                return helper(f1, f2, n - 1)

        return helper(0, 1, n)

