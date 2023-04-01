class Solution:
    def helper(self, cur, bit):
        if len(cur) == len(self.nums):
            self.answer.append(cur.copy())
            return 
        
        for i in range(len(self.nums)):
            check = 1 << i
            if not check & bit:
                bit |= check
                cur.append(self.nums[i])
                self.helper(cur, bit)
                bit ^= check
                cur.pop()


    def permute(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.answer = []
        self.helper([], 0)

        return self.answer
      
        

        