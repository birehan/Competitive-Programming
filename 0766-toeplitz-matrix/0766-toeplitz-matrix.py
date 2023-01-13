class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        dic = defaultdict(int)
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if r-c in dic and dic[r-c] != matrix[r][c]:
                    return False
                dic[r-c] =  matrix[r][c]
        
        return True