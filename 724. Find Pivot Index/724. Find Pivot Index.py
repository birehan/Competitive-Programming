from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pre = 0
        for i in range(len(nums)):
            nums[i] = pre + nums[i]
            pre = nums[i]

        for i in range(len(nums)):
            pre = nums[i - 1] if i - 1 >= 0 else 0
            cur = nums[len(nums) - 1] - nums[i]
            if pre == cur:
                return i

        return -1

