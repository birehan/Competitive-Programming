class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for a, b, c in times:
            graph[a].append((b, c))

        heap = [(0, k)]
        visited = set()

        while heap:
            cost, cur = heappop(heap)

            if cur in visited:
                continue
            
            visited.add(cur)

            if len(visited) == n:
                return cost
            
            
            for b, cur_cost in graph[cur]:
                heappush(heap, (cur_cost + cost, b))

        return -1

            
