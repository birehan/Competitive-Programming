class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dic = defaultdict(int)
        dic[0] = 1
        prefix = 0
        count = 0
        for num in nums:
            prefix += num
            if prefix%k in dic:
                count += dic[prefix%k] 
            dic[prefix%k] += 1
        
        return count