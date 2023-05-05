class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapify(heap)
        while len(heap) > 1:
            a = heappop(heap)
            b = heappop(heap)

            if a != b:
                heappush(heap, - abs(a - b))
        
        return abs(heap[0]) if heap else 0