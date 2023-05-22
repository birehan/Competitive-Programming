from typing import List
from collections import deque, defaultdict


from typing import List


class Solution:
    def minimumTime(self, n : int,m : int, edges : List[List[int]]) -> int:
        graph = defaultdict(list)
        Indegree = defaultdict(int)
        visited = set([i for i in range(1, n+1)])
        
        for a, b in edges:
            graph[a].append(b)
            Indegree[b] += 1
            
            if b in visited:
                visited.remove(b)
        
        queue = deque(list(visited))
        answer = [1 for i in range(n)]
        
      
        time = 0
        
        while queue:
            time += 1
            for _ in range(len(queue)):
                cur = queue.popleft()
                answer[cur-1] = str(time)
                for child in graph[cur]:
                    Indegree[child] -= 1
                    
                    if Indegree[child] == 0 and child not in visited:
                        visited.add(child)
                        queue.append(child)
            
        
        return " ".join(answer)
