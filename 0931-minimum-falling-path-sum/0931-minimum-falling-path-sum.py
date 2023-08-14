class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)

        def getValue(r, c):
            if not (0 <= r < n and 0 <= c < n):
                return inf
            
            return matrix[r][c]
        
        for r in range(1, n):
            for c in range(n):
                matrix[r][c] += min(
                    getValue(r - 1, c + 1),
                    getValue(r - 1, c),
                    getValue(r - 1, c - 1)
                )

        return min(matrix[-1])

        