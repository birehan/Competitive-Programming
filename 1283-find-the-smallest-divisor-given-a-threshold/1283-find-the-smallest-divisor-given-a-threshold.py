class Solution:
    def compute(self, nums, divisor):
        value_sum = 0
        for num in nums:
            value_sum += ceil(num/divisor)

        return value_sum

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left, right = 0, max(nums) + 1
        while right > left + 1:
            mid = (left+right)//2
            if self.compute(nums, mid) <= threshold:
                right = mid
            else:
                left = mid
        
        return right