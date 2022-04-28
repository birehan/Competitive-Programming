class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        result = []

        def right():
            for i in matrix[0]:
                result.append(i)
            matrix.pop(0)

        def down():
            for i in range(len(matrix)):
                result.append(matrix[i][-1])
                matrix[i].pop(-1)

        def left():
            for i in range(len(matrix[-1]) - 1, -1, -1):
                result.append(matrix[-1][i])
            matrix.pop(-1)

        def up():
            for i in range(len(matrix) - 1, -1, -1):
                result.append(matrix[i][0])
                matrix[i].pop(0)

        moves = [right, down, left, up]
        move_index = 0
        while matrix and matrix[0]:
            print(result, matrix)
            move_index = move_index % 4
            move = moves[move_index]
            move()
            move_index += 1

        return result
