class Solution:
    def uniquePaths(self, row: int, col: int) -> int:
        grid = [[0 for i in range(col)] for _ in range(row)]

        def getValue(r, c):
            if 0 <= r < row and 0 <= c < col:
                return grid[r][c]
            return 0

        for i in range(row):
            for j in range(col):
                grid[i][j] = getValue(i-1, j) + getValue(i, j-1)
                if i == 0 and j == 0:
                    grid[i][j] = 1

        return grid[row-1][col-1]
        