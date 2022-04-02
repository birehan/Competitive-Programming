class Solution(object):
    def maxOperations(self, nums, k):
        nums.sort()
        left, right, operation = 0, len(nums) - 1, 0
        while left < right:
            if nums[left] + nums[right] == k:
                left += 1
                right -= 1
                operation += 1
            elif nums[left] + nums[right] < k:
                left += 1
            else:
                right -= 1
        return operation
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
