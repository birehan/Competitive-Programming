class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = defaultdict(list)

        for i, (x1, y1, r1) in enumerate(bombs):
            for j in range(i+1, len(bombs)):
                x2, y2, r2 = bombs[j]
                distance = sqrt((x2-x1)**2 + (y2-y1)**2)
                if distance <= r1:
                    graph[i].append(j)
                
                if distance <= r2:
                    graph[j].append(i)
        
        def dfs(start, visited):
            if start in visited:
                return 0

            count = 1
            visited.add(start)
            for neighbor in graph[start]:
                count += dfs(neighbor, visited)
        
            return count

        max_bomb= 0
        for i in range(len(bombs)):
            max_bomb = max(max_bomb, dfs(i, set()))
        
        return max_bomb