class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        self.minTotalTime = 0
        graph = defaultdict(list)
        visited = set()

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(node):
            if node in visited:
                return 0
            
            visited.add(node)
            cost = 0
            
            for child in graph[node]:
                child_cost = dfs(child)
                cost += child_cost
            
            if (hasApple[node] or cost) and node != 0:
                cost += 2
            
            return cost
        
        return dfs(0)