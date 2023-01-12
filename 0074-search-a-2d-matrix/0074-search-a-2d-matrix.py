class Solution:
    def findRow(self, target, matrix):
        top, bottom = 0, len(matrix)
        while top < bottom:
            mid = (bottom + top)//2
            if target > matrix[mid][-1] :
                top = mid + 1
            elif target < matrix[mid][0]:
                bottom = mid - 1
            else: return mid
        return top
    
    def findCol(self, array, target):
            left, right = 0, len(array)
            while left < right:
                mid = (left + right)//2
                if target > array[mid] :
                    left = mid + 1
                elif target < array[mid]:
                    right = mid - 1
                else: return mid
            return left

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        row = self.findRow(target, matrix)
        if row >= len(matrix): return False

        col = self.findCol(matrix[row], target)
        if col >= len(matrix[0]): return False

        return matrix[row][col] == target