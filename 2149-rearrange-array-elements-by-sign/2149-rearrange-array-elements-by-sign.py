class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive, negative = [], []
        ans = []
        
        for i in nums:
            if i > 0: positive.append(i)
            else: negative.append(i)

        for i in range(len(nums)//2):
            ans.append(positive[i])
            ans.append(negative[i])

        return ans
