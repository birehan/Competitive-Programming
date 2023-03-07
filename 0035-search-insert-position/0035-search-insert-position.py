class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = -1, len(nums)
        while right > left + 1:
            mid = (right + left) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid
        
        return right
        