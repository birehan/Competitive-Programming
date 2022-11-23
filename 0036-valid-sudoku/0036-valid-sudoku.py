class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        dic = {}
                
        for row in range(len(board)):
            for col in range(len(board[row])):
            
                if board[row][col] != '.':
                    val = board[row][col]
                    r_key = ("row", row, val)
                    c_key = ("col", col, val)
                    sub_key = (row//3, col//3, val)
                    
                    if (r_key in dic) or (c_key in dic) or (sub_key in dic):
                        return False
                    else:
                        dic[r_key], dic[c_key], dic[sub_key] = val, val, val
                
        
        return True
        