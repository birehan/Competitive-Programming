class Solution(object):
    def sortColors(self, nums):
        for j in range(len(nums)):
            for i in range(len(nums)):
                if nums[i] == 0:
                    nums.insert(0, nums.pop(i))
                elif nums[i] == 2:
                    nums.insert(len(nums), nums.pop(i))
        return nums

