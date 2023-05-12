class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
      
        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
        
        queue = deque()
        for key, value in graph.items():
            if len(value) == 1:
                queue.append(key)
    
        while queue:
            lastLevel = queue.copy()
            for _ in range(len(queue)):
                cur = queue.popleft()
                for child in graph[cur]:
                    if cur in graph[child]:
                        graph[child].remove(cur)
                    if len(graph[child]) == 1:
                        queue.append(child)
            
            if not queue:
                return list(lastLevel)
        
        return [0]
