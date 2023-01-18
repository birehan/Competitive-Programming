class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        l  = len(nums)
        for i in range(l):
            cur = int(str(nums[i])[::-1])
            nums.append(cur)
        return len(set(nums))