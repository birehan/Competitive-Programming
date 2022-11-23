class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = count_zero = 0
        max_length = 0

        for right, value in enumerate(nums):
            if not value: count_zero += 1

            while count_zero > 1 and left < right:
                if nums[left] == 0: count_zero -= 1
                left += 1

            if count_zero == 1:
                max_length = max(max_length, right - left)

        if count_zero == 0:
            return len(nums)-1
        return max_length
