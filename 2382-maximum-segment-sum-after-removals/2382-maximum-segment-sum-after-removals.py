class Solution:
    def union(self, a, b):
        rootA, rootB = self.find(a), self.find(b)

        if self.rank[rootA] < self.rank[rootB]:
            rootA, rootB = rootB, rootA
        
        self.rank[rootA] += self.rank[rootB]
        self.root[rootB] = self.root[rootA]

        self.summ[rootA] += self.summ[rootB]
    
    def find(self, a):
        if self.root[a] != a:
            self.root[a] = self.find(self.root[a])
        return self.root[a]

    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        self.root = [i for i in range(len(nums))]
        self.rank = [1] * len(nums)
        self.summ = [0] * len(nums)
        max_sum = 0

        answer = [0]
        for i in range(len(removeQueries)-1, 0, -1):
            self.summ[removeQueries[i]] += nums[removeQueries[i]]
            # merge with right

            if removeQueries[i] < len(nums)-1 and self.summ[removeQueries[i]+1]:
                self.union(removeQueries[i], removeQueries[i]+1)

            # merge with left
            if removeQueries[i] > 0 and self.summ[removeQueries[i]-1]:
                self.union(removeQueries[i], removeQueries[i]-1)

            max_sum = max(max_sum, self.summ[self.find(removeQueries[i])])
            
            answer.append(max_sum)

        return reversed(answer)

        