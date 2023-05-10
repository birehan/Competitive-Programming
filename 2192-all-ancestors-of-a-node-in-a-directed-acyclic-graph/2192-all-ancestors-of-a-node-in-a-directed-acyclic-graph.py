class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(set)
        source = set([i for i in range(n)])
        Indegree = defaultdict(int)

        for a, b in edges:
            graph[a].add(b)
            Indegree[b] += 1
            if b in source:
                source.remove(b)
        
        ancestors = defaultdict(set)
        queue = deque(list(source))
        visited = source

        while queue:
            cur = queue.popleft()
            
            for neighbor in graph[cur]:
                Indegree[neighbor] -= 1
                ancestors[neighbor] = ancestors[neighbor].union(ancestors[cur])
                ancestors[neighbor].add(cur)
                if not Indegree[neighbor] and neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
        
        answer = [sorted(ancestors[i]) for i in range(n)]
        return answer

        