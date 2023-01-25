class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        index = len(nums1)-1
        while n > 0:
            if m > 0 and nums1[m-1] > nums2[n-1]:
                nums1[index] = nums1[m-1]
                index -= 1
                m -= 1
            else:
                nums1[index] = nums2[n-1]
                index -= 1
                n -= 1