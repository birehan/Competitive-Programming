class Solution:
    def union(self, a, b):
        rootA = self.find(a)
        rootB = self.find(b)
       
        if self.size[rootA] >= self.size[rootB]:
            self.size[rootA] += self.size[rootB]
            self.root[rootB] = self.root[rootA]
        else:
            self.size[rootB] += self.size[rootA]
            self.root[rootA] = self.root[rootB]
        
    def find(self, a):
        if self.root[a] != a:
            self.root[a] = self.find(self.root[a])

        return self.root[a]

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        self.root = [i for i in range(len(accounts))]
        self.size = [1] * len(accounts)

        for i in range(len(accounts)):
            for j in range(i+1, len(accounts)):
                if len(set(accounts[i]).intersection(set(accounts[j]))) > 1:
                    self.union(i, j)

        visited = set()
        answer = defaultdict(set)

        for i in range(len(accounts)):
            root_i = self.find(i)
            answer[root_i] =  answer[root_i].union(accounts[i][1:])
        
        answer = [[accounts[key][0]] + sorted(list(value)) for key, value in answer.items()]
        
        return answer

        