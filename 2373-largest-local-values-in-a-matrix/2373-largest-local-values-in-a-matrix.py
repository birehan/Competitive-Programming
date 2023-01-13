class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        row = col = len(grid)

        dirs = [[0, 0], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]

        max_local = [[0 for _ in range(col-2)] for _ in range(row-2)]

        def get_grid_max(r, c):
            max_val = 0
            for i, j in dirs:
                max_val = max(max_val, grid[r+i][c+j])
            return max_val

        for r in range(row-2):
            for c in range(col-2):
                max_local[r][c] = get_grid_max(r+1, c+1)

        
        return max_local

