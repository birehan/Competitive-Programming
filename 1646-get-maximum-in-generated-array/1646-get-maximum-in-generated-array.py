class Solution:
    def helper(self, n, dp):        
        if n not in dp:
            if n % 2 == 0:
                dp[n] = self.helper(n//2, dp)
            else:
                dp[n] = self.helper(n//2, dp) + self.helper(n//2+1, dp)

        return dp[n] 

    def getMaximumGenerated(self, n: int) -> int:
        if n < 2: return n

        dp = [0, 1] + [0] * 99
        for i in range(2, n+1):
            if not dp[i]:
                self.helper(i, dp)

        return max(dp)
       