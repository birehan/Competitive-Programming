class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        Indegree = defaultdict(int)
        relations = defaultdict(list)
        source = set([i for i in range(numCourses)])

        for a, b in prerequisites:
            relations[b].append(a)
            Indegree[a] += 1
            if a in source:
                source.remove(a)

        queue = deque(list(source))
        visited = source

        while queue:
            cur = queue.popleft()
            for neighbor in relations[cur]:
                if neighbor not in visited:
                    Indegree[neighbor] -= 1
                    if not Indegree[neighbor]:
                        visited.add(neighbor)
                        queue.append(neighbor)
                    
                if neighbor in visited and Indegree[neighbor] != 0:
                    return False
        
        return len(visited) == numCourses
                    