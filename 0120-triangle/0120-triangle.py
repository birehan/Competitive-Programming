class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                top = triangle[i-1][j] if 0 <= j < len(triangle[i-1]) else inf
                topLeft = triangle[i-1][j-1] if 0 <= j-1 < len(triangle[i-1]) else inf
                triangle[i][j] += min(top, topLeft)
            
        return min(triangle[-1])

        