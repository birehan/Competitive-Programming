class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start, end = -1, -1
        left, right = -1, len(nums)

        while right > left + 1:
            mid = (right + left)//2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid
        
        if right != len(nums) and nums[right] == target:
            start = right
        
        left, right = -1, len(nums)
        while right > left + 1:
            mid = (right + left)//2
            if nums[mid] <= target:
                left = mid
            else:
                right = mid
        
        if left != -1 and nums[left] == target:
            end= left
        
        return [start, end]