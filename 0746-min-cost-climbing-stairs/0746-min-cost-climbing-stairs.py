class Solution:
    def helper(self, n, dp):
        if n in  [0, 1]:
            return self.cost[n]
        
        if n not in dp:
            dp[n] = self.cost[n] + min(self.helper(n-1, dp), self.helper(n-2, dp))
        return dp[n]

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self.cost = [0] + cost + [0]
        dp = defaultdict(int)
        
        self.helper(len(self.cost)-1, dp)
        return dp[len(self.cost)-1]

        
      
            
        
            
            
        