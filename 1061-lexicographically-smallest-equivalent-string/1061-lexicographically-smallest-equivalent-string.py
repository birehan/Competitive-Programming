class Solution:
    def union(self, a, b):
        rootA, rootB = self.find(a), self.find(b)
        if rootA == rootB:
            return
        
        if rootA < rootB:
            self.root[rootB] = rootA
        else:
            self.root[rootA] = rootB
    
    def find(self, a):
        if a not in self.root:
            self.root[a] = a

        if self.root[a] != a:
            self.root[a] = self.find(self.root[a])
        return self.root[a]

    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        self.root = {}

        for i in range(len(s1)):
            self.union(s1[i], s2[i])

        ans = []
        for s in baseStr:
            ans.append(self.find(s))
        
        return "".join(ans)
        