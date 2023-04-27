class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        queue = deque([[[0, 0, 0, 0], 0]])
        visited = set()

        

        while queue:
            lock, cost = queue.popleft()

            lockString = "".join(map(str, lock))
            if lockString in visited:
                continue
            
            if lockString in deadends:
                continue
            
            if lockString == target:
                return cost

            visited.add(lockString) 

            for i in range(4):
                down = lock.copy()
                down[i] -= 1
                if down[i] == -1:
                    down[i] = 9

                queue.append([down, cost+1])

                up = lock.copy()
                up[i] += 1
                if up[i] == 10:
                    up[i] = 0

                queue.append([up, cost+1])
            
        return -1
                
                

        