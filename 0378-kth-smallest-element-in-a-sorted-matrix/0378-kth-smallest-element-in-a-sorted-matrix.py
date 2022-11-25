class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        left, right, length = matrix[0][0], matrix[-1][-1], len(matrix)
        def helper(value):
            count = 0
            for row in matrix:
                count += bisect_right(row, value)
            return count
        
        while left < right:
            mid = (left+right)//2
            if helper(mid) < k:
                left = mid + 1
            else: 
                right = mid
        
        return left


        