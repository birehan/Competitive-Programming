class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        row, col = len(grid2), len(grid2[0])
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = set()
        subIslands = 0

        def dfs(r, c, valid):
            visited.add((r, c))

            for a, b in dirs:
                new_r, new_c = a + r, b + c
                if not (0 <= new_r < row and 0 <= new_c < col):
                    continue
                
                if (new_r, new_c) in visited or (not grid2[new_r][new_c]):
                    continue

                x = dfs(new_r, new_c, valid)
                valid = valid and grid1[new_r][new_c] and x
                                
            ans =  valid and grid1[r][c]

            return ans

        for i in range(row):
            for j in range(col):
                if grid2[i][j] and (i, j) not in visited:
                    if dfs(i, j, 1):
                        subIslands += 1
            
        return subIslands