from typing import List

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums = sorted(nums)

        count = 0

        left = 0
        result = []

        while left < len(nums):
            cur = nums[left]

            if not result or cur > result[-1]:
                result.append(cur)
            else:
                dif = 1 + result[-1] - cur
                count += dif
                result.append(cur + dif)

            left += 1

        return count

