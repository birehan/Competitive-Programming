from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = nums.copy()
        for i in range(1, len(nums)):
            nums[i] *= nums[i - 1]
            res[len(nums) - i - 1] *= res[len(nums) - i]

        for i in range(len(nums)):
            l = nums[i - 1] if i > 0 else 1
            r = res[i + 1] if i + 1 < len(nums) else 1
            res[i] = l * r
        return res

