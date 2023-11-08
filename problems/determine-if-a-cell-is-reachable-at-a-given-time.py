class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        row, col = abs(sx-fx), abs(sy-fy)
        if row == col == 0 and t == 1:
            return False
        
        if max(row, col) <= t:
            return True
        
        return False