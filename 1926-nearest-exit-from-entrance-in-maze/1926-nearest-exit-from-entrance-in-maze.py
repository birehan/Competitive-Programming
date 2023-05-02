class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        visited = set([(entrance[0], entrance[1])])
        row, col = len(maze), len(maze[0])
        queue = deque([entrance])
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        level = 0
        while queue:
            length = len(queue)
            level += 1
            for _ in range(length):
                r, c = queue.popleft()
                for i, j in dirs:
                    new_r, new_c = r + i, c + j
                    if 0 <= new_r < row and 0 <= new_c < col and (new_r, new_c) not in visited and maze[new_r][new_c] == ".":
                        if new_r in [0, row-1] or new_c in [0, col-1]:
                            return level
                        visited.add((new_r, new_c))
                        queue.append((new_r, new_c))
        
        return -1
