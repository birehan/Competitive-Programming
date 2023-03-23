class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        dic = defaultdict(list)
        for a, b, distance in roads:
            dic[a].append([b, distance])
            dic[b].append([a, distance])

        visited = set()
        self.min_dist = inf

        def helper(cur):
            if cur in visited:
                return
            
            visited.add(cur)

            for v, dis in dic[cur]:
                self.min_dist = min(self.min_dist, dis)
                helper(v)   


        helper(1)
        
        
        return self.min_dist
