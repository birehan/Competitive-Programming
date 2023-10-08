class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        value = 0
        heaters.sort()

        for i in range(len(houses)):
            index = bisect_left(heaters, houses[i])
            if index >= len(heaters):
                dis = abs(heaters[-1] - houses[i])
            elif index == 0:
                dis = abs(heaters[0] - houses[i])
            else:
                dis = min(abs(heaters[index] - houses[i]), abs(heaters[index-1] - houses[i]))
            
            value = max(value, dis)
    
        return value

