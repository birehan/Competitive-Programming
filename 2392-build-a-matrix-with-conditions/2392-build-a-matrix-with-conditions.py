class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        positions = defaultdict(list)

        def helper(conditions):
            graph = defaultdict(list)
            indegree = defaultdict(int)
            source = set([i for i in range(1, k+1)])

            for a, b in conditions:
                graph[a].append(b)
                indegree[b] += 1

                if b in source:
                    source.remove(b)
            
            queue = deque(list(source))
            level = 0
            while queue:
                cur = queue.popleft()
                positions[cur].append(level)

                for child in graph[cur]:
                    indegree[child] -= 1
                    if not indegree[child]:
                        queue.append(child)
                
                level += 1
            
            return True if level == k else False
            
        if not helper(rowConditions): return []
        if not helper(colConditions): return []

        answer = [[0 for i in range(k)] for _ in range(k)]
        for key, value in positions.items():
            answer[value[0]][value[1]] = key

        return answer


        



