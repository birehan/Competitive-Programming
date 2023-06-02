class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [1] + [0] * (len(s))
        for i in range(len(s)):
            if s[i] != '0':
                dp[i+1] += dp[i]

            if i > 0 and  s[i-1] != '0' and 1 <= int(s[i-1] + s[i]) <= 26:
                dp[i+1] += dp[i-1]

        return dp[-1]


            
        