class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        length = 3 
        def is_valid(i, j):
            if i+2 < row and j+2 < col:
                return True
            return False
        
        def get_sum(i, j):
            cur_sum = grid[i+1][j+1]
            for k in range(length):
                cur_sum += grid[i][j+k]
                cur_sum += grid[i+length-1][j+k]
            return cur_sum

        max_sum = 0
        for i in range(row):
            for j in range(col): 
                if is_valid(i, j):
                    max_sum = max(get_sum(i, j), max_sum)
        
        return max_sum
                    
       