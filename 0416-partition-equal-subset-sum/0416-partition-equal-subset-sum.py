class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        summ = sum(nums)

        if summ % 2 != 0:
            return False
        
        @cache
        def dfs(total, index):
            if index >= len(nums):
                return False

            if total == summ//2:
                return True
            
            if dfs(total + nums[index], index + 1):
                return True
            
            if dfs(total, index + 1):
                return True
        
        return dfs(0, 0)

        