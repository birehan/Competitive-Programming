class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        min_dis = float('inf')
        index = -1
        for i in range(len(points)):
            a, b = points[i]
            if a == x or b == y:
                dis = abs(x-a) + abs(y-b)
                if dis < min_dis:
                    min_dis = dis
                    index = i
        
        return index