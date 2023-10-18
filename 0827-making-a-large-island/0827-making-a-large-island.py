class Solution:
    def union(self, a, b):
        rootA, rootB = self.find(a), self.find(b)

        if rootA == rootB:
            return self.rank[rootA]
        
        if self.rank[rootA] >= self.rank[rootB]:
            self.root[rootB] = self.root[rootA]
            self.rank[rootA] += self.rank[rootB]
            return self.rank[rootA]

        else:
            self.root[rootA] = self.root[rootB]
            self.rank[rootB] += self.rank[rootA]
            return self.rank[rootB]
    
    def find(self, a):
        if a not in self.root:
            self.root[a] = a
            self.rank[a] = 1
            
        if self.root[a] != a:
            self.root[a] = self.find(self.root[a])
        
        return self.root[a]

    def largestIsland(self, grid: List[List[int]]) -> int:
        self.root = {}
        self.rank = {}
        max_value = 1


        n = len(grid)
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    for r, c in dirs:
                        new_r, new_c = i + r, j + c
                        if 0 <= new_r < n and 0 <= new_c < n and grid[new_r][new_c]:
                            max_value = max(max_value, self.union((i, j), (new_r, new_c)))

        for i in range(n):
            for j in range(n):
                if not grid[i][j]:
                    roots = set()
                    total = 1
                    for r, c in dirs:
                        new_r, new_c = i + r, j + c
                        if 0 <= new_r < n and 0 <= new_c < n and grid[new_r][new_c]:
                            roots.add(self.find((new_r, new_c)))
                    
                    for root in roots:
                        total += self.rank[root]
                    
                    max_value = max(max_value, total)

        return max_value
                    
                    

                        
        