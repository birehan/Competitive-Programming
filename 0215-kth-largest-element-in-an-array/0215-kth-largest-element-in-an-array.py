class Solution:
    def helper(self, left, right):
        pivot = randint(left, right-1)
        self.nums[pivot], self.nums[left] =  self.nums[left], self.nums[pivot]
        
        pivot = left
        write = left+1

        for read in range(left+1, right):
            if self.nums[read] < self.nums[pivot]:
                self.nums[read], self.nums[write] =  self.nums[write], self.nums[read]
                write += 1

        self.nums[write-1], self.nums[pivot] =  self.nums[pivot], self.nums[write - 1]
        
        if len(self.nums) - self.k  == write-1:
            return
        elif len(self.nums) - self.k > write-1:
            self.helper(write, right)
        else:
            self.helper(left, write-1)


    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.nums = nums
        self.k = k
        self.helper(0, len(nums))

        return self.nums[-k]
        # quick select until you find pivot_index == n-k

   

