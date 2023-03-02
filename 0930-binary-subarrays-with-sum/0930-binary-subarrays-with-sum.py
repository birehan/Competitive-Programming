class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        dic = defaultdict(int)
        dic[0] = 1
        cur_sum = total = 0
        
        for num in nums:
            cur_sum += num
            total += dic[cur_sum - goal]
            dic[cur_sum] += 1
        
        return total