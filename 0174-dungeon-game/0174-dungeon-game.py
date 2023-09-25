class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        row, col = len(dungeon), len(dungeon[0])
        dungeon.append([inf] * (col + 1) )
        dungeon[-1][-2] = 1

        for r in range(row-1, -1, -1):
            dungeon[r].append(inf)
            for c in range(col-1, -1, -1):
                dungeon[r][c] = max(1, min(dungeon[r+1][c], dungeon[r][c+1]) - dungeon[r][c])
    
        
        return dungeon[0][0]
        