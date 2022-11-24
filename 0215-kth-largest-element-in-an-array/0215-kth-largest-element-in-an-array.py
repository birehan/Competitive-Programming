class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res = heapq.nlargest(k, nums)
        return res[-1]
        
     