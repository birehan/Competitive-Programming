class Solution:
    def union(self, a, b):
        rootA = self.find(a)
        rootB = self.find(b)
       
        if rootA <= rootB:
            self.root[rootB] = self.root[rootA]
        else:
            self.root[rootA] = self.root[rootB]
        
    def find(self, a):
        if self.root[a] != a:
            self.root[a] = self.find(self.root[a])

        return self.root[a]


    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        offset = 97
        self.root = dict([(chr(i+offset), chr(i+offset)) for i in range(26)])
        
        for i in range(len(s1)):
            self.union(s1[i], s2[i])
        
        answer = []
        for b in baseStr:
            answer.append(self.find(b))
        
        return "".join(answer)
        

        

        