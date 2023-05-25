class Solution:
    def union(self, a, b):
        rootA, rootB = self.find(a), self.find(b)
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
        if  self.root[a] != a:
            self.root[a] = self.find(self.root[a])
        
        return self.root[a]

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        joints = []
        self.root = [i for i in range(len(points))]
        self.rank = [1 for i in range(len(points))]
        

        for i in range(len(points)):
            for j in range(len(points)):
                distance = abs(points[j][0] - points[i][0]) + abs(points[j][1] - points[i][1])
                joints.append((distance, i, j))
    
        joints.sort()
        totalCost = 0
        for cost, a, b in joints:
            if self.union(a, b):
                totalCost += cost 
        
        return totalCost

        
        # a, b, c, d, e
        