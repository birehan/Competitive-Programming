class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:

        graph = defaultdict(list)
        for i in range(1, len(parent)):
            graph[parent[i]].append(i)
        
        visited = set()
        self.longest = 0
        
        def dfs(root):
            if root in visited:
                return 0
            
            visited.add(root)

            max_path_1 = max_path_2 = 0
            for child in graph[root]:
                child_path = dfs(child)

                if s[child] != s[root]:
                    if max_path_1 < child_path:
                        max_path_2 = max_path_1
                        max_path_1 = child_path

                    elif max_path_2 < child_path:
                        max_path_2 = child_path

            self.longest = max(self.longest, 1 + max_path_1 + max_path_2)
            return max_path_1 + 1
        

        dfs(0)
        return self.longest