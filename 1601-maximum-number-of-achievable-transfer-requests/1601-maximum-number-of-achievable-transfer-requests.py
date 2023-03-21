class Solution:
    def helper(self, index, count, dic):
        if all(v == 0 for v in dic.values()):
            self.max_count = max(self.max_count, count)
        
        if index == len(self.requests):
            return
        
        fromi, toi = self.requests[index]
        dic[fromi] -= 1
        dic[toi] += 1
        self.helper(index+1, count+1, dic)
        dic[fromi] += 1
        dic[toi] -= 1
        self.helper(index+1, count, dic)

    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        dic = defaultdict(int)
        self.max_count = 0
        self.requests = requests
        self.helper(0, 0, dic)
        
        return self.max_count
