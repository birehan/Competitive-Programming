class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        moves = {
                1: [(0, -1), (0, 1)], 
                2: [(-1, 0), (1, 0)],
                3: [(0, -1), (1, 0)],
                4: [(0, 1), (1, 0)],
                5: [(0, -1), (-1, 0)],
                6: [(0, 1), (-1, 0)]}
        
        row, col = len(grid), len(grid[0])
        visited = {(0, 0)}
        queue = deque([(0, 0)])
        is_valid = lambda i, j:  0 <= i < row and 0 <= j < col and (i, j) not in visited

        while queue:
            for _ in range(len(queue)):
                r, c =  queue.popleft()
                if r == row -1 and c == col -1:
                    return True
                for i, j in moves[grid[r][c]]:
                    new_r, new_c = r + i, c + j
                    if is_valid(new_r, new_c) and (-i, -j) in moves[grid[new_r][new_c]]:    
                
                        visited.add((new_r, new_c))
                        queue.append((new_r, new_c))

        
        return False