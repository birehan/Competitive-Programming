class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        # 
        dic = defaultdict(int)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                diff = nums[j] - nums[i]
                dic[(diff, j)] = dic.get((diff, i), 1) + 1

        return max(dic.values()) 
