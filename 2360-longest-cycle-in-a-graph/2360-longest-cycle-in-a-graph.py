class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        graph = defaultdict(list)
        Indegree = defaultdict(int)
        visited = set([i for i in range(len(edges))])

        for index, value in enumerate(edges):
            graph[index].append(value)
            Indegree[value] += 1

            if value in visited:
                visited.remove(value)
            
        queue = deque(list(visited))
        
        while queue:
            cur = queue.popleft()
            for child in graph[cur]:
                Indegree[child] -= 1

                if Indegree[child] == 0 and child not in visited:
                    visited.add(child)
                    queue.append(child)
        

        max_cycle = -1
        for i in range(len(edges)):
            if i not in visited:
                
                cycle_length = 1
                start = i

                while edges[start] != i:
                    visited.add(start)
                    start = edges[start]
                    cycle_length += 1
                
                max_cycle = max(max_cycle, cycle_length)
        return max_cycle


            

        
        
        
        

        