class Solution(object):
    def targetIndices(self, nums, target):
        swap_number = 0
        for n in range(len(nums), 0, -1):
            for i in range(n):
                if (n > 1) and (nums[i] > nums[i + 1]):
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                    swap_number += 1
                n -= 1
        result = []
        for i in range(len(nums)):
            if nums[i] == target:
                result.append(i)

        return result

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
