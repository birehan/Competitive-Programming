class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-p for p in piles]
        heapify(heap)

        while k:
            k -= 1
            cur = math.floor(heappop(heap)/2)
            heappush(heap, cur)
        
        return abs(sum(heap))
      