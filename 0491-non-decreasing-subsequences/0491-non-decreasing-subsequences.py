class Solution:
    def helper(self, cur, index):
        if index == len(self.nums):
            if len(cur) > 1:
                self.result.add(tuple(cur))
            return
        
        if not cur or cur[-1] <= self.nums[index]:
            cur.append(self.nums[index])
            self.helper(cur, index+1)
            cur.pop()
        
        self.helper(cur, index+1)

    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.result = set()
        self.nums = nums
        self.helper([], 0)

        return self.result
       