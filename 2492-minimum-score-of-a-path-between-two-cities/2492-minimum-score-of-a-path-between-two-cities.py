class Solution:
    def union(self, a, b, cost):
        rootA, rootB = self.find(a), self.find(b)
        
        if self.rank[rootA] <= self.rank[rootB]:
            self.rank[rootA] = min(self.rank[rootA], self.rank[rootB], cost)
            self.root[rootB] = self.root[rootA]
        else:
            self.rank[rootB] = min(self.rank[rootA], self.rank[rootB], cost)
            self.root[rootA] = self.root[rootB]
        
    def find(self, a):
        if self.root[a] != a:
            self.root[a] = self.find(self.root[a])

        return self.root[a]



    def minScore(self, n: int, roads: List[List[int]]) -> int:
        self.root = [i for i in range(n+1)]
        self.rank = [inf] * (n+1)
        self.min_cost = inf

        
        for a, b, cost in roads:
            self.union(a, b, cost)
        
        return self.rank[self.find(n)]
