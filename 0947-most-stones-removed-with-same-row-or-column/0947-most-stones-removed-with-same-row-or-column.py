class Solution:
    def union(self, a, b):
        rootA, rootB = self.find(a), self.find(b)

        if rootA == rootB:
            return
       
        if self.rank[rootA] >= self.rank[rootB]:
            self.rank[rootA] += self.rank[rootB]
            self.root[rootB] = self.root[rootA]
        else:
            self.rank[rootB] += self.rank[rootA]
            self.root[rootA] = self.root[rootB]
        
    def find(self, a):
        if self.root[a] != a:
            self.root[a] = self.find(self.root[a])

        return self.root[a]

    def removeStones(self, stones: List[List[int]]) -> int:
        self.root = dict([(i, i) for i in range(len(stones))])
        self.rank = dict([(i, 1) for i in range(len(stones))])

        for i in range(len(stones)):
            for j in range(i+1, len(stones)):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    self.union(i, j)
        visited = set()
        removedStones = 0
        for i in range(len(stones)):
            root_i = self.find(i) 
            if root_i not in visited:
                removedStones += self.rank[root_i] -1 
                visited.add(root_i)
        
        return removedStones
                