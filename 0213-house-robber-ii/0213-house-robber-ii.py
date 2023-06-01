class Solution:
    def helper(self, n, nums):
        if n == 0:
            return nums[0]

        if n == 1:
            return max(nums[0], nums[1])
            
        if self.dp[n] == -1:
            self.dp[n] = max(self.helper(n-1, nums), self.helper(n-2, nums) + nums[n])
        return self.dp[n]


    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        self.dp = [-1] * len(nums)
        val1 =  self.helper(len(nums)-2, nums[:-1])

        self.dp = [-1] * len(nums)
        val2 =  self.helper(len(nums)-2, nums[1:])

        return max(val1, val2)

        