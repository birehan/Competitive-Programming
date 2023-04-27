class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        
        row = col = len(grid)
        queue = deque([(0, 0, 1)])
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [-1, -1], [1, -1], [-1, 1]]
        visited = set()

        while queue:
            r, c, distance = queue.popleft()
            if (r,  c) in visited:
                continue
                
            visited.add((r, c))
            if r == row -1 and c == col -1:
                return distance
            for i, j in dirs:
                new_r, new_c = r + i, c + j
                if (0 <= new_r < row and 0 <= new_c < col) and  grid[new_r][new_c] == 0:
                    queue.append((new_r, new_c, distance + 1))
        
        return -1