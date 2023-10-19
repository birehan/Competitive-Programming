class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        graph = defaultdict(list)
        for a, b, time in meetings:
            graph[a].append([b, time])
            graph[b].append([a, time])
        
        for node in graph:
            graph[node].sort(key=lambda x:x[1])
        
        queue = deque([0, firstPerson])
        time = [inf] * n
        time[0] = time[firstPerson] = 0
        visited = set([0, firstPerson])

        while queue:
            node = queue.popleft()
            for child, child_time in graph[node]:
                if child_time >= time[node]:
                    if child_time < time[child]:
                        time[child] = child_time
                        queue.append(child)
                        visited.add(child)
        
        return visited
        