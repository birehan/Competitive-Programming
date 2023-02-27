class Solution:
    def maxTurbulenceSize(self, nums: List[int]) -> int:
        max_len = 1
        left, right = 0, 1
        inc = None

        for right in range(len(nums)):
            dif = nums[right] - nums[right-1]
            if dif < 0 and (inc==None or inc==True):
                inc = False
            elif dif > 0 and (inc==None or inc == False):
                inc = True
            elif dif == 0:
                left = right
                inc = None
            else:
                left = right-1
                
            max_len =max(right - left + 1, max_len)
        
        return max_len  