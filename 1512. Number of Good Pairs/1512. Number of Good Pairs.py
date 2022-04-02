from collections import Counter


class Solution(object):
    def numIdenticalPairs(self, nums):
        count = 0
        counter = Counter(nums)
        for key in counter:
            count += ((counter[key]) * (counter[key] - 1)) // 2
        return count
        """
        :type nums: List[int]
        :rtype: int
        """
