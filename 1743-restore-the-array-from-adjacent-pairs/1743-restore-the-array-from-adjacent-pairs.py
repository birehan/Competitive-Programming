class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for a, b in adjacentPairs:
            graph[a].append(b)
            graph[b].append(a)
        
        queue = deque()
        answer = []
        visited = set()
        
        for key, value in graph.items():
            if len(value) == 1:
                queue.append(value[0])
                answer.append(key)
                visited.add(key)
                break
        
        
        while queue:
            cur = queue.popleft()
            visited.add(cur)
            answer.append(cur)

            for child in graph[cur]:
                if child not in visited:
                    queue.append(child)
        
        return answer


        


        