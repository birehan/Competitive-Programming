class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dic = {}
        total = 0
        for i in nums:
            cur = dic.get(i, 0)
            total += cur
            dic[i] = cur + 1
        
        return total