class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:

        graph = defaultdict(list)
        for i in range(len(edges)):
            graph[edges[i][0]].append((edges[i][1], succProb[i]))
            graph[edges[i][1]].append((edges[i][0], succProb[i]))
        
        visited = set()
        heap = [(-1, start_node)]

        while heap:
            prob, node = heappop(heap)
            
            if node == end_node:
                return abs(prob)
            
            if node in visited:
                continue
            
            visited.add(node)
        
            for child, edge_prob in graph[node]:
                if child not in visited:
                    heappush(heap, (-(abs(prob) * edge_prob), child))
        
        return 0
            

        