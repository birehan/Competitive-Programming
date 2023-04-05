class Solution:
    def backtracking(self, bit, index, change):
        if bit != None and change:
            self.count[bit] += 1

        if index >= len(self.nums):
            return
      
        self.backtracking(bit, index+1, False)
        if bit == None:
            self.backtracking(self.nums[index], index+1, True)
        else:
            self.backtracking(bit | self.nums[index], index+1, True)
            
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        self.count = defaultdict(int)
        self.nums = nums
        self.backtracking(None, 0, False)

        return max(self.count.values())