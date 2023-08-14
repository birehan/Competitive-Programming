class Solution:
    @cache
    def dfs(self, r, c, k):
        if not (0 <= r < self.n and 0 <= c < self.n):
            return 0
        
        if k == 0:
            return 1
        
        return 0.125 * (
            self.dfs(r + 2, c + 1, k-1) + 
            self.dfs(r + 2, c - 1, k-1) + 
            self.dfs(r - 2, c + 1, k-1) + 
            self.dfs(r - 2, c - 1, k-1) + 
            self.dfs(r + 1, c + 2, k-1) + 
            self.dfs(r + 1, c - 2, k-1) + 
            self.dfs(r - 1, c + 2, k-1) + 
            self.dfs(r - 1, c - 2, k-1) 
        )


    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        self.n = n
        return self.dfs(row, column, k)
        