class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, sufix = [1], [0]*len(nums)
        cur = 1
        for i in nums:
            cur *= i
            prefix.append(cur)
        cur = 1
        for i in range(len(nums)-1, -1, -1):
            cur *= nums[i]
            sufix[i] = cur
        sufix.append(1)
        
        answer = []
       
        for i in range(len(nums)):
            answer.append(prefix[i] * sufix[i+1])
        
        return answer

     


       