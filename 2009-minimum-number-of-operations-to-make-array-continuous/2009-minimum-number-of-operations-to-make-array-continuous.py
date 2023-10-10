class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        nums = list(sorted(set(nums)))
        cost = inf

        for i in range(len(nums)):
            index = bisect_right(nums, nums[i] + n - 1)
            cost = min(cost, n - (index - i))
        
        return cost

