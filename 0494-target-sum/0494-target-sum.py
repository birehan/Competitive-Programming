class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dic = Counter()
        dic[nums[0]] += 1
        dic[-nums[0]] += 1

        for i in range(1, len(nums)):
            dic1 = Counter()
            for key, value in dic.items():
                dic1[key+nums[i]] += value
            
            for key, value in dic.items():
                dic1[key-nums[i]] += value
            
            dic = dic1
     
        return dic[target]
        