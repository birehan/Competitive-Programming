class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        index = 0
        while index < len(nums):
            connect = nums[index] - 1
            if index != connect and 0 <= connect  < len(nums) and nums[index] != nums[connect]:
                nums[index], nums[connect] = nums[connect], nums[index]
            else:
                index += 1
        
        for i in range(len(nums)):
            if i + 1 != nums[i]:
                return i+1

        return len(nums)+1