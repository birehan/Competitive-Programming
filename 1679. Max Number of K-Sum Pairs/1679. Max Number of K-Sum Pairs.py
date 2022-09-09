from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r = 0 , len(nums)-1
        max_operation = 0
        while l < r:
            summ = nums[l] + nums[r]
            if summ == k:
                max_operation += 1
                l += 1
                r -= 1
            elif summ < k:
                l += 1
            else:
                r -= 1
        return max_operation