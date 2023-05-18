class Solution:
    def union(self, a, b):
        rootA = self.find(a)
        rootB = self.find(b)
       
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


    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        self.root = [i for i in range(n)]
        self.rank = [1] * n

        for a, b in edges:
            self.union(a, b)
        
        return self.find(source) == self.find(destination)

       
        