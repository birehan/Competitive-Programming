class Solution:
    def conquer(self, num1, num2, nums):
        p2 = len(num2) - 1
        for p1 in range(len(num1)-1, -1, -1):
            while p2 >= 0 and nums[num1[p1]] <= nums[num2[p2]]:
                p2 -= 1
            
            self.answer[num1[p1]] += 1 + p2
        
        merged = []
        p1, p2 = 0 , 0 
        while p1 < len(num1) and p2 < len(num2):
            if nums[num1[p1]] < nums[num2[p2]]:
                merged.append(num1[p1])
                p1 += 1
            else:
                merged.append(num2[p2])
                p2 += 1
        
        merged.extend(num1[p1:] or num2[p2: ])

        return merged


    def divide(self, left, right,nums):
        if left + 1 == right:
            return [left]
        
        mid = (left + right)//2
        left_a = self.divide(left, mid,nums)
        right_a = self.divide(mid, right,nums)

        return self.conquer(left_a, right_a,nums)


    def countSmaller(self, nums: List[int]) -> List[int]:
        self.answer = [0] * len(nums)
        self.divide(0, len(nums),nums)

        return self.answer
        