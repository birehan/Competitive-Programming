# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        length =  mountain_arr.length()
        left, right = -1, length
        ans = -1

        while left + 1 < right:
            mid = (left + right)//2
            if mid == 0:
                ans = 1
                break
            l_val, mid_val, r_val = mountain_arr.get(mid-1),  mountain_arr.get(mid),  mountain_arr.get(mid+1)
            if l_val < mid_val > r_val:
                ans = mid
                break
            elif l_val < mid_val < r_val:
                left = mid
            else:
                right = mid
        
        left, right = -1, ans+1
        while left + 1 < right:
            mid = (left + right)//2
            if mountain_arr.get(mid) <= target:
                left = mid
            else:
                right = mid
        
        if left != -1 and mountain_arr.get(left) == target:
            return left
        
        left, right = ans, length
        while left + 1 < right:
            mid = (left + right)//2
            if mountain_arr.get(mid) >= target:
                left = mid
            else:
                right = mid
        
        if mountain_arr.get(left) == target:
            return left

        return -1


        

        