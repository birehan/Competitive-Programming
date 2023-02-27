class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        min_num = nums[0]
        stack = []
        
        for num in nums[1:]:
            while stack and stack[-1][1] <= num:
                stack.pop()
            
            if stack and stack[-1][0] < num:
                return True
            
            stack.append([min_num, num])
            min_num = min(min_num, num)
        
        return False