class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        answer = []
        row, col = len(mat), len(mat[0])
        dic = {True:[[-1, 1], [0, 1], [1, 0]],False:[[1, -1], [1, 0], [0, 1]]}

        r, c = 0, 0
        is_up = True
        
        while r < row  or c < col:
            answer.append(mat[r][c])
            
            for i, j in dic[is_up]:
                nr, nc = i+r, j+c
                if 0 <= nr < row and 0 <= nc < col:
                    is_up = abs(i)==abs(j) if is_up else (not abs(i)==abs(j))
                    r, c = nr, nc
                    break
            else: break

        return answer