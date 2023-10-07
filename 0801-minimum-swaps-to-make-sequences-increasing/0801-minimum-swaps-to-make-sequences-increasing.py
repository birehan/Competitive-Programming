class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        start = {}
        a, b = nums1[0], nums2[0]
        start[(a, b)] = min( start.get((a, b), inf), 0)
        start[(b, a)] = min(start.get((b, a), inf), 1)
        

        for i in range(1, n):
            a, b = nums1[i], nums2[i]
            new_start = {}
            for c, d in start.keys():
                cost = start[(c, d)]
                if a > c and b > d:
                    new_start[(a, b)] = min(new_start.get((a, b), inf), cost)
                
                if a > d and b > c:
                    new_start[(b, a)] = min(new_start.get((b, a), inf), cost + 1)
            
            start = new_start

        return min(start.values()) if start else 0



