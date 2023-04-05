class Solution:
    def find_gcd(self, num1, num2):
        num1, num2 = max(num1, num2), min(num1, num2)
        while num2:
            num1, num2 = num2, num1 % num2
        
        return num1

    def subarrayGCD(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            cur_gcd = nums[i]
            for j in range(i+1, len(nums)):
                cur_gcd = self.find_gcd(cur_gcd,nums[j])
                if cur_gcd == k:
                    count += 1
               
            if nums[i] == k:
                count += 1
        
        return count