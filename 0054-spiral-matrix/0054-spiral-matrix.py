class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        values = []
        row, col = len(matrix), len(matrix[0])
        count = row * col
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        index = 0

        r, c = 0, -1

        while count:
            i, j = dirs[index]
            while 0 <= r+i < row and 0 <= c+j < col and matrix[r+i][c+j] != -101:
                values.append(matrix[r+i][c+j])
                matrix[r+i][c+j] = -101
                r, c = r + i, c + j
                count -= 1
                
            index += 1
            index %= 4
        
        return values

