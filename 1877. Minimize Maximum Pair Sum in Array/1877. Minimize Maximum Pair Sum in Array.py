class Solution(object):
    def minPairSum(self, nums):
        nums.sort()
        if len(nums) == 0:
            return 0
        l, r = 0, len(nums) - 1

        result = 0
        while l < r:
            result = max(result, (nums[l] + nums[r]))
            l += 1
            r -= 1


        return result

        """
        :type nums: List[int]
        :rtype: int
        """
