class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        index = 0

        while index < len(nums):
            connect = nums[index]
            if connect != index and connect < len(nums):
                nums[connect], nums[index] = nums[index], nums[connect]
            else:
                index += 1
        
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        
        return len(nums)