class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set([0])

        def dfs(node):
            
            count = 0
            cur_sum = values[node]

            for child in graph[node]:
                if child not in visited:
                    visited.add(child)
                    child_count, child_sum = dfs(child)
                    cur_sum += child_sum
                    count += child_count
            
            if cur_sum % k == 0:
                return count + 1, 0
            else:
                return count, cur_sum
        
        count, summ =  dfs(0)
        return count



        