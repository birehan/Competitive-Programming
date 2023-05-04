class Solution:

    def getEmpty(self, board):
        for i in range(2):
            for j in range(3):
                if board[i][j] == 0:
                    return (i, j)
        
        return (-1, -1)
                

    def slidingPuzzle(self, board: List[List[int]]) -> int:
        queue = deque([board])

        visited = [board]

        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        answer = [[1, 2, 3], [4, 5, 0]]
        row, col = 2, 3


        def compute(curBoard):
            empty = self.getEmpty(curBoard)

            nextBoards = []
            for i, j in dirs:
                new_r, new_c = i + empty[0], j + empty[1]
            
                if 0 <= new_r < row and 0 <= new_c < col:
                    newBoard = deepcopy(curBoard)
                    newBoard[empty[0]][empty[1]], newBoard[new_r][new_c] = newBoard[new_r][new_c], newBoard[empty[0]][empty[1]]
                    if newBoard not in visited:
                        visited.append(newBoard)
                        nextBoards.append(newBoard)
            return nextBoards
                    

        moves = 0
        while queue:
            length = len(queue)
            for _ in range(length):
                curBoard = queue.popleft()
                if curBoard == answer:
                    return moves
                
                queue.extend(compute(curBoard))
                
            moves += 1
        
        return -1