class Solution:
    def union(self, a, b):
        rootA, rootB = self.find(a), self.find(b)
        if rootA != rootB:
               

            if self.rank[rootA] >= self.rank[rootB]:
             
                self.rank[rootA] += self.rank[rootB]
                self.root[rootB] = self.root[rootA]

                if self.answer[rootA] == []:
                    self.answer[rootA] = [False, False]
                
                if self.answer[rootB] != []:
                    self.answer[rootA][0] = self.answer[rootB][0] or self.answer[rootA][0]
                    self.answer[rootA][1] = self.answer[rootB][1] or self.answer[rootA][1]

                if a[1] == 1 or b[1] == 1:
                    self.answer[rootA][0] = True
                
                if a[1] == self.col  or b[1] == self.col :
                    self.answer[rootA][1] = True

                if self.answer[rootA][0] and self.answer[rootA][1]:
                    return False
                

            else:
                self.rank[rootB] += self.rank[rootA]
                self.root[rootA] = self.root[rootB]

                if self.answer[rootB] == []:
                    self.answer[rootB] = [False, False]

                if self.answer[rootA] != []:
                    self.answer[rootB][0] = self.answer[rootB][0] or self.answer[rootA][0]
                    self.answer[rootB][1] = self.answer[rootB][1] or self.answer[rootA][1]

                
                if a[1] == 1 or b[1] == 1:
                    self.answer[rootB][0] = True
                
                if a[1] == self.col  or b[1] == self.col:
                    self.answer[rootB][1] = True
                
                if self.answer[rootB][0] and self.answer[rootB][1]:
                    return False
            
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


       