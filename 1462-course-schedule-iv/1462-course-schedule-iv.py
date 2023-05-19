class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[b].append(a)

        dependency = defaultdict(set)
        visited = set()
        
        def helper(node):
            if node in visited:
                return dependency[node]

            visited.add(node)

            cur = set(graph[node] if graph[node] else [node])      
            for root in graph[node]:
                root_dep =  helper(root)
                cur = cur.union(root_dep)
            
            dependency[node] = cur
            return cur
        
        for i in range(numCourses):
            if i not in visited:
                helper(i)

        for i in range(len(queries)):
            queries[i] = queries[i][0] in dependency[queries[i][1]]
        
        return queries

