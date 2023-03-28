class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        index = 0
        while index < len(nums):
            connect = nums[index] - 1
            if connect != index and nums[connect] != nums[index]:
                nums[index], nums[connect] = nums[connect], nums[index]
            else:
                index += 1
            
        for i in range(len(nums)):
            if i + 1 != nums[i]:
                return [nums[i], i + 1]