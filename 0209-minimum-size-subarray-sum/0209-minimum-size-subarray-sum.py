class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        max_length = float('inf')
        left = summ = 0
        for right in range(len(nums)):
            summ += nums[right]
            while summ >= target and left <= right:
                max_length = min(max_length, right-left+1)
                summ -= nums[left]
                left += 1
        
        return max_length if max_length != float('inf') else 0
