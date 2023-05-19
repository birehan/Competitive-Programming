class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        Indegree = defaultdict(int)
        source = set([i for i in range(numCourses)])

        for a, b in prerequisites:
            graph[a].append(b)
            Indegree[b] += 1

            if b in source:
                source.remove(b)

        queue = deque(list(source))
        dependency = defaultdict(set)
        while queue:
            cur = queue.popleft()
            for child in graph[cur]:
                Indegree[child] -= 1
                dependency[child] = dependency[child].union(dependency[cur])
                dependency[child].add(cur)

                if not Indegree[child]:
                    queue.append(child)
        
        for i in range(len(queries)):
            queries[i] = queries[i][0] in dependency[queries[i][1]]
        
        return queries

