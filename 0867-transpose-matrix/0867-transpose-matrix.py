class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row = len(matrix)
        column = len(matrix[0])
        transposed = [[0 for _ in range(row)] for _ in range(column)]
       
        for r in range(row):
            for c in range(column):
                transposed[c][r] = matrix[r][c]


                
        return transposed

     