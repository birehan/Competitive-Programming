class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zero_row, zero_col = [], []
        row, col = len(matrix), len(matrix[0])

        for r in range(row):
            for c in range(col):
                if matrix[r][c] == 0:
                    zero_row.append(r)
                    zero_col.append(c)
        
        for r in range(row):
            for c in range(col):
                if r in zero_row or c in zero_col:
                    matrix[r][c] = 0
            
    