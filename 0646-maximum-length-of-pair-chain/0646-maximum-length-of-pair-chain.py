class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        n = len(pairs)
        dp = [1] * n

        for i in range(1, n):
            cur_max = 0
            for j in range(i-1, -1, -1):
                if  pairs[i][0] > pairs[j][1]:
                    cur_max = max(cur_max, dp[j])
            
            dp[i] += cur_max
        
        return max(dp)