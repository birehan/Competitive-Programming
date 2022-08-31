from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r = 0, 0
        res, total = 0, k

        while r < len(nums):
            total += nums[r]

            while nums[r] * (r - l + 1) > total:
                total -= nums[l]
                l += 1
            res = max(res, r - l + 1)
            r += 1

        return res