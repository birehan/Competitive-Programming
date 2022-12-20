class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
     
        for i in range(len(nums1)-1, -1, -1):
            if m and n:
                if nums1[m-1] > nums2[n-1]:
                    nums1[i] = nums1[m-1]
                    m -= 1
                else:
                    nums1[i] = nums2[n-1]
                    n -= 1
            elif n:
                nums1[i] = nums2[n-1]
                n -= 1
