class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.matrix[i][j] += self.get(i-1, j) + self.get(i, j-1) - self.get(i-1, j-1)
      
    
    def get(self, row, col):
        if 0 <= row < len(self.matrix) and 0 <= col < len(self.matrix[0]):
            return self.matrix[row][col]
        return 0
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.get(row2, col2) - self.get(row1-1, col2) - self.get(row2, col1-1) + self.get(row1-1, col1-1)


        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)???\
