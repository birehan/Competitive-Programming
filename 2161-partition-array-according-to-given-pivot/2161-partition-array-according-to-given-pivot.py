class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        answer = [pivot] * len(nums)
        left, right = 0, len(nums)-1
        
        for i in range(len(nums)):
            if nums[i] < pivot:
                answer[left] = nums[i]
                left += 1

            if nums[-i-1] > pivot:
                answer[right] = nums[-i-1]
                right -= 1
        
        return answer