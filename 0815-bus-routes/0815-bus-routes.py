class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        buses = defaultdict(list)
        for i in range(len(routes)):
            for stop in routes[i]:
                buses[stop].append(i)

        queue = deque(buses[source])
        visited = set(buses[source])
        level = 0

        while queue:
            length = len(queue)
            level += 1

            for _ in range(length):

                curBus = queue.popleft()
                print(curBus)
                for stop in routes[curBus]:

                    if stop == target:
                        return level

                    for bus in buses[stop]:
                        if bus not in visited:
                            visited.add(bus)
                            queue.append(bus)
            
        return -1
                    
                    