class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        row, col = len(mat), len(mat[0])
        if row * col != r * c: return mat

        reshape = []
        cur_col = []
        for i in range((row)):
            for j in range((col)):
                cur_col.append(mat[i][j])
                if len(cur_col) == c:
                    reshape.append(cur_col)
                    cur_col = []
        
        return reshape
        