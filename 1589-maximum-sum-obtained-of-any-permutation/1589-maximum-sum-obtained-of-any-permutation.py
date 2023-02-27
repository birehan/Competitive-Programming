class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        freqency = [0] * (n+1)
        total = 0

        for start, end in requests:
            freqency[start] += 1
            freqency[end+1] -= 1
        
        freqency = list(accumulate(freqency))
        nums.sort(reverse = True)
        freqency.sort(reverse = True)

    
        for i in range(n):
            total += freqency[i] * nums[i]
        
        return (total % (10**9 + 7))