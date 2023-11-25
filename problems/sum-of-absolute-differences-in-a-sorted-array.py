class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        forward, backward = [0] * n, [0] * n
        for i in range(1, len(nums)):
            forward[i] = forward[i-1] + (i * abs(nums[i] - nums[i-1]))
        
        for i in range(len(nums)-2, -1, -1):
            backward[i] = backward[i+1] + (n - i - 1) * abs(nums[i] - nums[i+1])
        
        return [forward[i] + backward[i] for i in range(n)]
