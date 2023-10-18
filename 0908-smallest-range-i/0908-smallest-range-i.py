class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        max_value, min_value = max(nums), min(nums)
        min_score = max_value - min_value

        for i in range(max_value + 1):
            cur_max = max(i, max_value - k)
            cur_min = min(i, min_value + k)
            
            min_score = min(min_score, cur_max - cur_min)
        
        return min_score
