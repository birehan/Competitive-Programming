class Solution:
    def helper(self, mainRoot, subRoot,a , b):
        if self.answer[mainRoot] == []:
            self.answer[mainRoot] = [False, False]

        if self.answer[subRoot] != []:
            self.answer[mainRoot][0] = self.answer[mainRoot][0] or self.answer[subRoot][0]
            self.answer[mainRoot][1] = self.answer[mainRoot][1] or self.answer[subRoot][1]

        
        if a[1] == 1 or b[1] == 1:
            self.answer[mainRoot][0] = True
        
        if a[1] == self.col  or b[1] == self.col:
            self.answer[mainRoot][1] = True
        
        if self.answer[mainRoot][0] and self.answer[mainRoot][1]:
            return False
        
        return True

    def union(self, a, b):
        rootA, rootB = self.find(a), self.find(b)
        if rootA != rootB:
            if self.rank[rootA] >= self.rank[rootB]:
                self.rank[rootA] += self.rank[rootB]
                self.root[rootB] = self.root[rootA]
                return self.helper(rootA, rootB, a, b)
            else:
                self.rank[rootB] += self.rank[rootA]
                self.root[rootA] = self.root[rootB]
                return self.helper(rootB, rootA, a, b)
            
        return True

    
    def find(self, a):
        if self.root[a] != a:
            self.root[a] = self.find(self.root[a])
        return self.root[a]

    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        self.root = defaultdict(int)
        self.rank = defaultdict(int)
        self.answer = defaultdict(list)
        self.col = col
        watered_cells = set()

        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, -1], [-1, 1], [1, -1]]
        
        time = 0
        for r, c in cells:
            self.root[(r, c)] = (r, c)
            self.rank[(r, c)] = 1

            for i, j in dirs:
                new_r, new_c = r + i, c + j
                if 1 <= new_r <= row and 1 <= new_c <= col and (new_r, new_c) in watered_cells:
                    if not self.union((r, c), (new_r, new_c)):
                        return time

            watered_cells.add((r, c))
            time += 1
        
        return time


       