class Solution:
    def union(self, a, b):
        rootA, rootB = self.find(a), self.find(b)

        if self.size[rootA] >= self.size[rootB]:
            self.root[rootB] = self.root[rootA]
            self.size[rootA] += self.size[rootB]
        else:
             self.root[rootA] = self.root[rootB]
             self.size[rootB] += self.size[rootA]

    
    def find(self, a):
        if self.root[a] != a:
            self.root[a] = self.find(self.root[a])
        
        return self.root[a]

    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        self.root = [i for i in range(len(s))]
        self.size = [1] * len(s)

        for a, b in pairs:
            self.union(a, b)
        
        dic = defaultdict(list)
        indices = defaultdict(list)

        for i in range(len(s)):
            root_i = self.find(i)
            dic[root_i].append(s[i])
            indices[root_i].append(i)

        answer = list(s)
        for key, value in dic.items():
            value.sort(reverse=True)
            for index in indices[key]:
                answer[index] = value.pop()

        return "".join(answer)


        