class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
      

        dirs = [[1, 0],[-1, 0], [0, 1], [0, -1]]
        row, col = len(image), len(image[0])
        visited = set()
        start = image[sr][sc]

        def dfs(sr, sc):
            if (not (0 <= sr < row and 0 <= sc < col)) or (sr, sc) in visited or image[sr][sc] != start:
                return

            visited.add((sr, sc))
            image[sr][sc] = color

            for i,j in dirs:
                dfs(sr+i, sc+j)

        dfs(sr, sc)
        return image