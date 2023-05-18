class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        grid = [0]
        direction = 1
        row =  len(board)
        for i in range(row-1, -1, -1):
            for j in range(row):
                if direction == 1:
                    grid.append(board[i][j])
                else:
                    grid.append(board[i][row-1-j])
            direction *= -1
        
        queue = deque([(1, 0)])
        visited = set([1])

        while queue:
            start, cost = queue.popleft()

            if start == row * row:
                return cost

            for i in range(start+1, min(start+7, row*row+1)):
                destination = grid[i] if grid[i] != -1 else i
                if destination not in visited:
                    visited.add(destination) 
                    queue.append((destination, cost+1))
                   
        
        return -1
