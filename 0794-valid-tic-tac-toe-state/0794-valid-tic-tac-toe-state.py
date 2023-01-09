class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        cnt = Counter("".join(board))
        wins_search_space = board + \
            list("".join(x) for x in zip(*board)) + \
            [
                "".join(board[i][i] for i in range(3)),
                "".join(board[i][2-i] for i in range(3)),
            ]
        X_wins = "XXX" in wins_search_space
        O_wins = "OOO" in wins_search_space

        if X_wins and O_wins:
            return False
        elif X_wins:
            return cnt["X"] - cnt["O"] == 1
        elif O_wins:
            return cnt["X"] - cnt["O"] == 0
        else:
            return 0 <= cnt["X"] - cnt["O"] <= 1
