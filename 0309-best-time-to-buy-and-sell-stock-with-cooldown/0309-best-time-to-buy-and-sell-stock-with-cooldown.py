class Solution:
    @cache
    def dfs(self, i, j):
        if i >= len(self.prices) or j >= len(self.prices):
            return 0
        
        if i == j:
            return self.dfs(i, j + 1)
        elif self.prices[i] >= self.prices[j]:
            return self.dfs(j, j + 1)
        else:
            profit = self.prices[j] - self.prices[i]
            return max(profit + self.dfs(j + 2, j + 2), self.dfs(i, j + 1))

    def maxProfit(self, prices: List[int]) -> int:
        self.prices = prices
        return self.dfs(0, 0)
        