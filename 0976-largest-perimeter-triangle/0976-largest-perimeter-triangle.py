class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)-1, 1, -1):
            two_side = nums[i-2] + nums[i-1]
            if two_side > nums[i]:
                return two_side + nums[i]
        return 0
        