class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        arrival_time = []
        for i in range(len(dist)):
            arrival_time.append(ceil(dist[i]/speed[i]))
        
        arrival_time.sort()
        time = 1

        for i in range(len(arrival_time)):
            if time > arrival_time[i]:
                return i
            
            time += 1
        
        return len(arrival_time)
           