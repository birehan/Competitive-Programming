class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        row = len(grid)
        dirs = [[1, 0], [-1, 0], [0, 1],[0, -1]]
        visited = set()

        def getConnected(r, c):
            stack = [(r, c)]
            visited.add((r, c))

            while stack:
                r, c = stack.pop()
                for i, j in dirs:
                    new_r, new_c = r + i, c + j
                    if 0 <= new_r < row and 0 <= new_c < row and grid[new_r][new_c] == 1 and (new_r, new_c) not in visited:
                        stack.append((new_r, new_c))
                        visited.add((new_r, new_c))
            
            return 1
        
        island = None
        for i in range(row):
            if island == None:
                for j in range(row):
                    if grid[i][j]:
                        island = getConnected(i, j)
                        break
            else: break

        level = 0
        island = deque(list(visited))
       
        while island:
            for _ in range(len(island)):
                r, c = island.popleft()

                for i, j in dirs:
                    new_r, new_c = r + i, c + j
                    if 0 <= new_r < row and 0 <= new_c < row and (new_r, new_c) not in visited:
                        if grid[new_r][new_c] == 1:
                            return level

                        island.append((new_r, new_c))
                        visited.add((new_r, new_c))

            level += 1

     
        
        