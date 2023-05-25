class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) <= 4:
            return 0
        
        a = nums[-1] - nums[3]
        b = nums[-4] - nums[0]
        c = nums[-2] - nums[2]
        d = nums[-3] - nums[1]

        return min(a, b, c, d)