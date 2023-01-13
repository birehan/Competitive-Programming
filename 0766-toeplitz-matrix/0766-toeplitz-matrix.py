class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for r in range(1, len(matrix),):
            for c in range(1, len(matrix[0])):
                if matrix[r-1][c-1] != matrix[r][c]:
                    return False
    
        return True