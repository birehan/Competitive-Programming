class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        dirs = [[1, 0], [-1, 0], [0, -1], [0, 1], [1, 1], [-1, 1], [1, -1], [-1, -1]]   
     
        res = []
        for dire in dirs:
            row, col = king[0], king[1]
            cur = []
            while 0  <= row < 8 and 0 <= col < 8:
                if [row, col] in queens:
                    cur = [row, col]
                    break
                row, col = row+dire[0], col+dire[1]

            if cur: res.append(cur)
        
        return res

