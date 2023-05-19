class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:

        for i in range(1, len(heights)):
            diff = heights[i] - heights[i-1]
            heights[i-1] = diff if diff > 0 else 0

        heights[-1] = 0

        heap = []
        position = 0

        while position < len(heights)-1:
            if heights[position] == 0:
                position += 1
            elif ladders > 0:
                heappush(heap, heights[position])
                position += 1
                ladders -= 1
            else:
                heappush(heap, heights[position])
                if heap[0] > bricks:
                    break
                bricks -= heappop(heap)
                position += 1
        
        return position 




        