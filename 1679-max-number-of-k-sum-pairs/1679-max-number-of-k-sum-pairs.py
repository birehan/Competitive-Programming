class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        operations = 0
        left, right = 0, len(nums)-1

        while left < right:
            if nums[left]+nums[right] > k:
                right -= 1
            elif  nums[left]+nums[right] < k:
                left += 1
            else:
                operations += 1
                left += 1
                right -= 1
            
        return operations      