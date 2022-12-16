class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        # compute the prefix sum
        for i in range(len(grid)):
            for j in range(1, len(grid[i])):
                grid[i][j] += grid[i][j-1]
        
        # compute the val
        def helper(r1, r2):
            res = 0
            for c in range(2, len(grid[0])):
                summ = 0
                for i in range(3):
                    if i != 1:
                        summ += grid[r1+i][c] - (grid[r1+i][c-3] if c >  2 else 0)
                    else:
                        summ += grid[r1+i][c-1] - grid[r1+i][c-2]
                res = max(res, summ)
            return res

        res = 0 
        for i in range(2, len(grid)):
            res = max(res, helper(i-2, i))
        
        return res

