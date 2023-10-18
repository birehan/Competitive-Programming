class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        max_value, min_value = max(nums), min(nums)
        return max(0, (max_value - k)- (min_value + k))
