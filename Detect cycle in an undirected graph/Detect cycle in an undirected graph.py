from typing import List
from collections import defaultdict, deque
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
	    visited = set()
    
            
        for i in range(V):
            if i not in visited:
                visited.add(i)
                Indegree = defaultdict(int)
                queue = deque([i])
                
                while queue:
                    cur = queue.popleft()
                 
                    
                    if Indegree[cur] > 1:
                        return 1
                    for neighbor in adj[cur]:
                        Indegree[neighbor] += 1
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)
        
        return 0
		#Code here
