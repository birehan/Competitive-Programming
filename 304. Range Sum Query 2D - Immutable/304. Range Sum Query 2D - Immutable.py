from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        for i in range(len(self.matrix)):
            for j in range(1, len(self.matrix[i])):
                matrix[i][j] += matrix[i][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        while row1 <= row2:
            res += self.matrix[row1][col2] -( self.matrix[row1][col1-1] if col1 > 0 else 0)
            row1 += 1
        return res