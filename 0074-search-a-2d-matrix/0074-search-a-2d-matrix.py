class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def search(left, right):
            if left > right:
                return False
            
            mid = (left + right) // 2
            row, col = mid // n, mid % n
            if matrix[row][col] > target:
                return search(left, mid-1)
            elif matrix[row][col] < target:
                return search(mid+1, right)
            else:
                return True
        
        m, n = len(matrix), len(matrix[0])
        return search(0, n * m - 1)