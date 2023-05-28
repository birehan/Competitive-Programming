class Solution:
    def tribonacci(self, n: int, dp=defaultdict(int)) -> int:
        if n == 0:
            return n
        
        if n in [1, 2]:
            return 1
        
        if n not in dp:
            dp[n] = self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
        
        return dp[n]

        