class Solution:
    def union(self, a, b, option):
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

    def equationsPossible(self, equations: List[str]) -> bool:
        offset = 97
        self.root = dict([(chr(i+offset), chr(i+offset)) for i in range(26)])
        self.rank = dict([(chr(i+offset), 1) for i in range(26)])

        for a, option1, option2, b in equations:
            if option1 == "=":
                self.union(a, b, option1)
        
        for a, option1, option2, b in equations:
            if option1 == "!":
                if self.find(a) == self.find(b):
                    return False
                    
        
        return True
        