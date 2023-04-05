class Solution:
    def findGCD(self, nums: List[int]) -> int:
        num1, num2 = min(nums), max(nums)
        while num2:
            num1, num2 = num2, num1 % num2
        
        return num1