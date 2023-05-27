class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        prefix = answer = 0
        for i in range(len(nums)):
            prefix += nums[i]
            answer = max(answer, ceil(prefix/(i+1)))
        
        return answer

        # 8, 7, 
        # 8  8 9 

        # 4 5, 8, 8, 9

        