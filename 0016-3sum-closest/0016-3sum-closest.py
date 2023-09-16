class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        
        for i in range(len(nums)-2):
            left = i + 1
            right = len(nums) - 1
    
            while left < right:
                summ = nums[i] + nums[left] + nums[right]   
                if abs(summ - target) < abs(result - target):
                    result = summ
                    
                if summ == target:
                    return summ
                
                if summ > target:
                    right -= 1
                else:
                    left += 1
        
        return result