class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ans = [[0 for _ in range(n)] for _ in range(m)]

        row_sum = []
        col_sum = []
        for i in range(m):
            row_sum.append( 2 * sum(grid[i]) - m)
            for j in range(n):
                if i > 0:
                    grid[i][j] += grid[i-1][j]
                if i == m -1:
                    col_sum.append(2 * grid[i][j] - n)

        for i in range(m):
            for j in range(n):
                ans[i][j] = row_sum[i] + col_sum[j]
      
        return ans