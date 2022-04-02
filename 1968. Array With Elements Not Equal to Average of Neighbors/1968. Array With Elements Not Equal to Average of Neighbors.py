class Solution(object):
    def rearrangeArray(self, nums):
        nums.sort()
        result = []
        while len(nums) != 0:
            result.append(nums.pop())
            if len(nums) != 0:
                result.append(nums.pop(0))
        return result
        """
        :type nums: List[int]
        :rtype: List[int]
        """
