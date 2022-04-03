from collections import Counter


class Solution(object):
    def topKFrequent(self, nums, k):
        nums = Counter(nums)
        keys_list = list(nums.keys())
        values_list = list(nums.values())
        result = []
        for i in range(k):
            val = max(values_list)
            ind = values_list.index(val)
            result.append(keys_list[ind])
            values_list[ind] = 0

        return result
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
