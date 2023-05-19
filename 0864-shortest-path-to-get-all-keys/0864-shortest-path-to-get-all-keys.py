class Solution:
    def shortestPathAllKeys(self, grid): 
        
        row, col = len(grid), len(grid[0])

        def getSource():
            source = None
            lettersCount = 0
            for i in range(row):
                for j in range(col):
                    if grid[i][j] == "@":
                        source =  [i, j]
                    if grid[i][j].islower():
                        lettersCount += 1

            return source, lettersCount
        
        def bitCount(num):
            bits = 0
            while num:
                bits += num & 1
                num >>= 1
            
            return bits
            
        
        source,lettersCount  = getSource()
        queue = deque([(source[0], source[1], 0, 0)])
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        visited = set()
        while queue:
            r, c, bit, level = queue.popleft()
            if (r, c, bit) in visited:
                continue
            
            if bitCount(bit) == lettersCount:
                return level
            
            visited.add((r, c, bit))
            for i, j in dirs:
                new_r, new_c = r + i, c + j
                if 0 <= new_r < row and 0 <= new_c < col and grid[new_r][new_c] != "#":
                    if grid[new_r][new_c] in ".@":
                        queue.append((new_r, new_c, bit, level+1))
                        
                    elif grid[new_r][new_c].islower():

                        position = 1 << (ord(grid[new_r][new_c]) - 97)
                        queue.append((new_r, new_c, bit | position, level+1))

                    elif grid[new_r][new_c].isupper():
                        position = 1 << (ord(grid[new_r][new_c].lower()) - 97)
                        if position & bit:
                            queue.append((new_r, new_c, bit, level+1))
        
        return -1




                        
                    


