class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        adjecents = defaultdict(list)
        for i , j in roads:
            adjecents[i].append(j)
            adjecents[j].append(i)

        max_rank = 0

        for i in range(n):
            for j in range(n):
                if i != j:
                    rank = len(adjecents[i]) + len(adjecents[j]) - (1 if i in adjecents[j] else 0)
                    max_rank = max(max_rank, rank)
        
        return max_rank






        