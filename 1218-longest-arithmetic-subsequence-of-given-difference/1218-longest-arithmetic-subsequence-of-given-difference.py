class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = defaultdict(int)

        for num in arr:
            count = 1 + dp[num]
            dp[num + difference] = count
        
        return max(dp.values())