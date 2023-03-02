class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        length = len(nums)
        result = [-1] * length

        nums = nums + nums

        for right, num in enumerate(nums):
            while stack and nums[stack[-1]] < num:
                ind = (stack.pop()) % length
                result[ind] = num
            stack.append(right)
        
        return result