class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:

        ops = [
            [[0, 0], [0, 1],[0, 2]], 
            [[1, 0], [1, 1], [1, 2]], 
            [[2, 0], [2, 1], [2, 2]], 
            [[0, 0], [1, 1], [2, 2]],  
            [[0, 2], [1, 1], [2, 0]], 
            [[0, 0], [1, 0], [2, 0]], 
            [[0, 1], [1, 1], [2, 1]], 
            [[0, 2], [1, 2], [2, 2]]
            ]
        
        row, col = len(grid), len(grid[0])

        def get_grid_sum(r, c):
            sums = set()
            for op in ops:
                cur_sum = set()
                for i, j in op:
                    if not (1 <= grid[r+i][c+j] < 10):
                        return False
                    cur_sum.add(grid[r+i][c+j])
                if len(cur_sum) != 3:
                    return False
                sums.add(sum(cur_sum))
            return len(sums) == 1

        magics = 0
        for r in range(row-2):
            for c in range(col-2):
                if get_grid_sum(r, c):
                    magics += 1
        
        return magics

       
      