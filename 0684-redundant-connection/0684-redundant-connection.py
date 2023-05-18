class Solution:
    def union(self, a, b):
        rootA = self.find(a)
        rootB = self.find(b)

        if rootA == rootB:
            return False

        if self.rank[rootA] >= self.rank[rootB]:
            self.rank[rootA] += self.rank[rootB]
            self.root[rootB] = self.root[rootA]
        else:
            self.rank[rootB] += self.rank[rootA]
            self.root[rootA] = self.root[rootB]
        
        return True
        
    def find(self, a):
        if self.root[a] != a:
            self.root[a] = self.find(self.root[a])

        return self.root[a]

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        answer = []
        self.root = [i for i in range(len(edges)+1)]
        self.rank = [1] * (len(edges)+1)

        for a, b in edges:
            if not self.union(a, b):
                return [a, b]        