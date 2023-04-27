class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        queue = deque([0])

        while queue:
            cur = queue.popleft()
            if cur in visited:
                continue
            
            visited.add(cur)
            queue.extend(rooms[cur])
        
        return len(visited) == len(rooms)
        