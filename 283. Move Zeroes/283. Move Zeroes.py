from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0
        right = 0
        while right < len(nums)-1 and left < len(nums)-1:
            if nums[left] == 0:
                while right < len(nums)-1 and nums[right] == 0:
                    right += 1
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            else:
                left += 1
                right += 1
