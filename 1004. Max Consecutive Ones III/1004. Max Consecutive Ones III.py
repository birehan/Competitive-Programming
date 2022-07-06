from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0
        count = 0
        max_count = 0
        while right < len(nums):
            if nums[right] == 1:
                right += 1
                count += 1
            elif nums[right] == 0 and k > 0:
                k -= 1
                right += 1
                count += 1
            else:
                if nums[left] == 0:
                    k += 1
                left += 1
                count -= 1

            if count > max_count:
                max_count = count

        return max_count
