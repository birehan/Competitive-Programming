class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        left, right = lower, upper
        for i in differences:
            left += i
            right += i
            left = max(left, lower)
            right = min(right, upper)
        
        res = right-left+1 
        return res if res > 0 else 0
        