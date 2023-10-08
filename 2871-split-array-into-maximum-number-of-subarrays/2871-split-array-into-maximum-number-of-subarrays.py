class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        min_score = nums[0]
        for i in range(1, len(nums)):
            min_score &= nums[i]
        
        cur_score = -1
        count = 0
        score_sum = 0

        for i in range(len(nums)):
            if cur_score == -1:
                cur_score = nums[i]
            else:
                cur_score &= nums[i]
            
            if score_sum +  cur_score  <= min_score:
                score_sum += cur_score
                count += 1
                cur_score = -1
        
        return count
