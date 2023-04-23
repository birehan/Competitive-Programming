class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        answer = [0] * n
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()
        def dfs(root):
            if root in visited:
                return Counter()
            
            visited.add(root)

            cur_count = Counter({labels[root]: 1})
            for child in graph[root]:
                cur_count += dfs(child)
            
            answer[root] = cur_count[labels[root]]
            return cur_count
        
        dfs(0)
        return answer