class Solution:
    def union(self, a, b):
        rootA, rootB = self.find(a), self.find(b)
        if self.rank[rootA] < self.rank[rootB]:
            rootA, rootB = rootB, rootA

        self.rank[rootA] += self.rank[rootB]
        self.root[rootB] = self.root[rootA]
            
    def find(self, a):
        if self.root[a] != a:
            self.root[a] = self.find(self.root[a])
        
        return self.root[a]

    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        self.root = [i for i in range(n)]
        self.rank = [1] * n

        answer = []
        for a, b in requests:
            rootA, rootB = self.find(a), self.find(b)
            cur = True
            for ra, rb in restrictions:
                rootRa, rootRb = self.find(ra), self.find(rb)
                if sorted([rootRa, rootRb]) == sorted([rootA, rootB]):
                    cur = False
                    break

            answer.append(cur)
            if cur:
                self.union(a, b)
        
        return answer

            
