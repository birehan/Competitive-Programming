class Solution:
    def helper(self, cur, index):
        self.answer.append(cur.copy())
        if index == len(self.nums):
            return
        for i in range(index, len(self.nums)):
            cur.append(self.nums[i])
            self.helper(cur, i+1)
            cur.pop()

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.answer = []
        self.nums = nums
        self.helper([], 0)
        return self.answer
        