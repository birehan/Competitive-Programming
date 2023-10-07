class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for a, b, cost in flights:
            graph[a].append((b, cost))

        heap = [(0, 0, src)]
        visited = set()

        # print(graph[1])

        while heap:
            cost, cur_k, node = heappop(heap)
            if (cur_k, node) in visited:
                continue


            if node == dst:
                return cost
            
        
            visited.add((cur_k, node))
            # print(node, graph[node])
            # print("visited: ", visited)
            for negh, negh_cost in graph[node]:
                plus_k = 0 if negh == dst else 1
                if (cur_k + plus_k, negh) not in visited and (cur_k < k or negh == dst):
                    heappush(heap, (negh_cost + cost, cur_k + plus_k, negh))

            
        
        return -1