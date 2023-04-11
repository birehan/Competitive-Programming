class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []
        path = [0]
        def dfs(start):

            if start == len(graph)-1:
                paths.append(path.copy())
                return
            
            for neighbor in  graph[start]:
                path.append(neighbor)
                dfs(neighbor)
                path.pop()
        
        dfs(0)
        return paths