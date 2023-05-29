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


    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        edges = sorted(edgeList, key=lambda x:x[2])
        sorted_queries = sorted([[v[0], v[1], v[2],i] for i, v in enumerate(queries)], key=lambda x:x[2])

        answer = [False] * len(queries)
        self.root = [i for i in range(n)]
        self.rank = [1] * n
        start = 0
        
        for a, b, limit, index in sorted_queries:
            while start < len(edges) and edges[start][2] < limit:
                l, r, cost = edges[start]
                start += 1
                self.union(l, r)
        
            if self.find(a) == self.find(b):
                answer[index] = True
        
        return answer
        

        

