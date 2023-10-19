class Solution:
    def union(self, a, b):
        rootA, rootB = self.find(a), self.find(b)
        if rootA == rootB:
            return
        
        if self.rank[rootA] >= self.rank[rootB]:
            self.root[rootB] = rootA
            self.rank[rootA] += self.rank[rootB]
        else:
            self.root[rootA] = rootB
            self.rank[rootB] += self.rank[rootA]
    
    def find(self, a):
        if a not in self.root:
            self.root[a] = a
            self.rank[a] = 1

        if self.root[a] != a:
            self.root[a] = self.find(self.root[a])
        return self.root[a]

    def numSimilarGroups(self, strs: List[str]) -> int:
        self.root = {}
        self.rank = {}

        for i in range(len(strs)):
            for j in range(i+1, len(strs)):
                index1, index2 = -1, -1
                valid = True
                for k in range(len(strs[i])):
                    if strs[i][k] != strs[j][k]:
                        if index1 == -1:
                            index1 = k
                        elif index2 == -1:
                            index2 = k
                        else:
                            valid = False
                            break
                
                if strs[i][index1] != strs[j][index2] or (strs[i][index2] != strs[j][index1]):
                    valid = False
                
                if valid:
                    self.union(strs[i], strs[j])
        
        roots = set()
        for string in strs:
            roots.add(self.find(string))
        
        return len(roots)
            
        