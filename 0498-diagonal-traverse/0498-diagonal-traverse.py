class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        answer = []
        row, col = len(mat), len(mat[0])
        dic = {
            1:[[-1, 1], [0, 1], [1, 0]],
            0:[[1, -1], [1, 0], [0, 1]]}

        r, c = 0, 0
        is_up = True
        
        while r < row  or c < col:
            answer.append(mat[r][c])
            
            for i, j in dic[int(is_up)]:
                nr, nc = i+r, j+c
                if 0 <= nr < row and 0 <= nc < col:
                    valid =  abs(i)==abs(j)
                    is_up = valid if is_up else not valid
                    r, c = nr, nc
                    break
                    
            else: break

        return answer