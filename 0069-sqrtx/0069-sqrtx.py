class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0,  (x+1)//2
        while left <= right:
            mid = (left + right)//2

            if mid * mid > x:
                right = mid - 1

            elif mid * mid <= x:
                left = mid + 1
       
        return left-1