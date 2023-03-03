class Solution: 
    def gridGame(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j] += grid[i][j-1] if j > 0 else 0
                
        n = len(grid[0])
        min_value = min(grid[0][-1]-grid[0][0], grid[1][n-2])

        for i in range(n-2):
            max_value = max(grid[1][i], grid[0][-1] - grid[0][i+1])
            min_value = min(min_value, max_value)
        
        return min_value
