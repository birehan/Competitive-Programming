class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        start = defaultdict(lambda:inf)
        a, b = nums1[0], nums2[0]
        start[(a, b)] = min(start[(a, b)] , 0)
        start[(b, a)] = min(start[(b, a)], 1)
        

        for i in range(1, n):
            a, b = nums1[i], nums2[i]
            new_start = defaultdict(lambda:inf)
            for c, d in start.keys():
                cost = start[(c, d)]
                if a > c and b > d:
                    new_start[(a, b)] = min(new_start[(a, b)], cost)
                
                if a > d and b > c:
                    new_start[(b, a)] = min(new_start[(b, a)], cost + 1)
            
            start = new_start

        return min(start.values()) if start else 0



