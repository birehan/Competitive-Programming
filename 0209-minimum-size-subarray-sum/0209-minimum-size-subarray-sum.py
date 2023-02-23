class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        min_len = inf
        cur_sum = 0
        for right, num in enumerate(nums):
            cur_sum += num
            while left <= right and cur_sum >= target:
                min_len = min(min_len, right - left + 1)
                cur_sum -= nums[left]
                left += 1

        return min_len if min_len != inf else 0       