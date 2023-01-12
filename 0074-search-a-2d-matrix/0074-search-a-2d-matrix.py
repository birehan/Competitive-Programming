class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def search(left, right):
            if left > right:
                return False
            middle = (left + right) // 2
            i, j = middle // n, middle % n
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                return search(middle + 1, right)
            else:
                return search(left, middle - 1)
        
       
        m, n = len(matrix), len(matrix[0])

        return search(0, m * n - 1)