class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for i in range(len(equations)):
            graph[equations[i][0]].append((equations[i][1], values[i]))
            graph[equations[i][1]].append((equations[i][0], 1/values[i]))
        


        answer = []
        for a, b in queries:
                
            visited = set([a])
            queue = deque([(a, 1)])
            ans = -1

            while queue:
                node, val = queue.popleft()

                if node == b:
                    if a not in graph:
                        ans = -1
                    else:
                        ans = val
                    break
                
                if node in graph:
                    for child,edge_val in graph[node]:
                        if child not in visited:
                            queue.append((child, val * edge_val))
                            visited.add(child)
            

            answer.append(ans)



        
        return answer