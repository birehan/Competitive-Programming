class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = set()
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def find_area(row, col):
            visited.add((row, col))

            areas = [(row, col)]
            for i, j in dirs:
                new_r, new_c = i + row, j + col
                if (0 <= new_r < len(board) and 0 <= new_c < len(board[0])) and (new_r, new_c) not in visited and board[new_r][new_c] == "O":
                    areas.extend(find_area(new_r, new_c))

            return areas
        
        def populate(areas):
            for row, col in areas:
                if  (row == 0 or row == len(board)-1) or (col == 0 or (col == len(board[0]) - 1)):
                    return
            
            for row, col in areas:
                board[row][col] = "X"

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O" and (i, j) not in visited:
                    areas = find_area(i, j)
                    populate(areas)
                    

        return board    


        # [["O","X","X","O","X"],
        #  ["X","O","O","X","O"],
        #  ["X","O","X","O","X"],
        #  ["O","X","O","O","O"],
        #  ["X","X","O","X","O"]]   


        #  [["O","X","X","O","X"],
        #   ["X","X","X","X","O"],
        #   ["X","X","X","O","X"],
        #   ["O","X","O","X","O"],
        #   ["X","X","O","X","O"]]