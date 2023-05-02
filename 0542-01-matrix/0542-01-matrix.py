class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row, col = len(mat), len(mat[0])
        queue = deque()
        visited = set()

        for i in range(row):
            for j in range(col):
                if not mat[i][j]:
                    queue.append((i, j))
                    visited.add((i, j))
        answer = [[0 for _ in range(col)] for _ in range(row)]

        level = 0
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while queue:
            length = len(queue)
            level += 1
            for _ in range(length):
                r, c = queue.popleft()
                for i, j in dirs:
                    new_r, new_c = r + i, c + j
                    if 0 <= new_r < row and 0 <= new_c < col and (new_r, new_c) not in visited:
                        answer[new_r][new_c] = level
                        queue.append((new_r, new_c))
                        visited.add((new_r, new_c))
        
        return answer
