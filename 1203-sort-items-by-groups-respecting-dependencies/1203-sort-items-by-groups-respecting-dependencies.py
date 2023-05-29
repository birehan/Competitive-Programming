class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:

        def helper(graph, indegree):
            queue = deque([i for i in range(len(graph)) if not indegree[i]])
            order = []

            while queue:
                cur = queue.popleft()
                order.append(cur)
                for child in graph[cur]:
                    indegree[child] -= 1
                
                    if not indegree[child]:
                        queue.append(child)
            
            return order if len(order) == len(graph) else []
        

        for u in range(len(group)):
            if group[u] == -1:
                group[u] = m
                m+=1

        graph_items = [[] for _ in range(n)]
        indegree_items = [0] * n
        graph_groups = [[] for _ in range(m)]
        indegree_groups = [0] * m  

        for node in range(n):
            for child in beforeItems[node]:
                graph_items[child].append(node)
                indegree_items[node] += 1

                if group[node] != group[child]:
                    graph_groups[group[child]].append(group[node])
                    indegree_groups[group[node]] += 1
        
        node_order = helper(graph_items, indegree_items)
        group_order = helper(graph_groups, indegree_groups)

        if not node_order or not group_order:
            return []
        
        in_group_order = defaultdict(list)
        for node in node_order:
            in_group_order[group[node]].append(node)
        
        answer = []
        for group in group_order:
            answer.extend(in_group_order[group])
        
        return answer


