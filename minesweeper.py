class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        visited = set()
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1]]

        if board[click[0]][click[1]] == "M":
            board[click[0]][click[1]] = "X"
            return board

        def countNeighborMines(row, col):
            count = 0
            for i, j in dirs:
                cur_r, cur_c = i + row, j + col
                if not (0 <= cur_r < len(board) and 0 <= cur_c < len(board[0])):
                    continue
                
                if board[cur_r][cur_c] == "M":
                    count += 1
            
            return count
        
        def dfs(row, col):
            visited.add((row, col))

            mineCount = countNeighborMines(row, col)

            if mineCount:
                board[row][col] = str(mineCount)
                return
            
            if board[row][col] == "E":
                board[row][col] = "B"
            
            for i, j in dirs:
                cur_r, cur_c = i + row, j + col
                if not (0 <= cur_r < len(board) and 0 <= cur_c < len(board[0])):
                    continue
                
                if (cur_r, cur_c) in visited:
                    continue
                
                dfs(cur_r, cur_c)
        
        dfs(click[0], click[1])
        return board