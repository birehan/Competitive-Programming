class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        index = 0

        while index < len(nums):
            connect = nums[index] - 1
            if connect != index and  nums[connect] != nums[index]:
                nums[connect], nums[index] = nums[index], nums[connect]
            else:
                index += 1
            
        answer = []
        for i in range(len(nums)):
            if nums[i] != i + 1:
                answer.append(i+1)
            
        return answer