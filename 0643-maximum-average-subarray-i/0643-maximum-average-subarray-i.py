class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur_sum = sum(nums[:k])
        max_avg = cur_sum/k

        for i in range(k, len(nums)):
            cur_sum -= nums[i-k]
            cur_sum += nums[i]
            max_avg = max(max_avg, cur_sum/k)

        return max_avg