class Solution:
    def union(self, a, b):
        rootA, rootB = self.find(a),self.find(b)
       
        if self.rank[rootA] < self.rank[rootB]:
            rootA, rootB = rootB, rootA

        self.rank[rootA] += self.rank[rootB]
        self.root[rootB] = self.root[rootA]
     
    def find(self, a):
        if self.root[a] != a:
            self.root[a] = self.find(self.root[a])

        return self.root[a]


    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        self.root = [i for i in range(len(source))]
        self.rank = [1] * len(source)

        for a, b in allowedSwaps:
            self.union(a, b)
        
        swapables = defaultdict(set)
        for i in range(len(source)):
            root_i = self.find(i)
            swapables[root_i].add(i)
        
        answer = 0
        for key, value in swapables.items():

            s = Counter([source[index] for index in value])
            t = Counter([target[index] for index in value])

            for item in t:
                if t[item] > s[item]:
                    answer += abs(s[item] - t[item])
    
        return answer
        

            

