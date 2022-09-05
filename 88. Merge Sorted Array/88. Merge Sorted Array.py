from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        l = len(nums1) - 1
        while nums2 and m:
            if nums2[-1] > nums1[m - 1]:
                nums1[l] = nums2.pop()
            else:
                nums1[l] = nums1[m - 1]
                m -= 1
            l -= 1

        while nums2:
            nums1[l] = nums2.pop()
            l -= 1


