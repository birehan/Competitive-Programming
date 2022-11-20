class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        
        def swap(l, r):
            nums[l], nums[r] = nums[r], nums[l]
        
        def reverse(l, r):
            while l < r:
                swap(l, r)
                l += 1
                r -= 1
        
        is_inc, inc = False, -1
        for i in range(len(nums)-1):
            if nums[i] <  nums[i+1]:
                inc = i
                is_inc = True
            else:
                is_inc = False
        
        if is_inc:
            return swap(inc, inc + 1)
        if inc == -1:
            return reverse(0, len(nums)-1)
        
        reverse(inc + 1, len(nums)-1)
        nex = inc + 1 
        for i in range(inc+1, len(nums)):
            if nums[i] > nums[inc]:
                nex = i
                break
                    
        swap(inc, nex)