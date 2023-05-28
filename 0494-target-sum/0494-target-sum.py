class Solution:
    def helper(self, index, cur_sum):
        if index == len(self.nums):
            if cur_sum == self.target: return 1
            return 0
        
        if (index, cur_sum) not in self.dp:
            self.dp[(index, cur_sum)] = self.helper(index+1, cur_sum - self.nums[index]) + self.helper(index+1, cur_sum + self.nums[index])
        
        return self.dp[(index, cur_sum)]

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
       self.nums = nums
       self.target = target
       self.dp = defaultdict(int)
       
       return self.helper(0, 0)
