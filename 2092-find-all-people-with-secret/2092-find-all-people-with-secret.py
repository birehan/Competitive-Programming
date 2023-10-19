class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        graph = defaultdict(list)
        for a, b, time in meetings:
            graph[a].append([b, time])
            graph[b].append([a, time])
       
        queue = deque([0, firstPerson])
        time = [inf] * n
        time[0] = time[firstPerson] = 0
        visited = set([0, firstPerson])

        while queue:
            node = queue.popleft()
            for child, child_time in graph[node]:
                if child_time >= time[node] and child_time < time[child]:
                    time[child] = child_time
                    queue.append(child)
                    visited.add(child)
        
        return visited
        