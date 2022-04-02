class Solution(object):
    def kthLargestNumber(self, nums, k):
        nums = sorted(list(map(int, nums)))
        result = str(nums[-k])
        return result
        """
        :type nums: List[str]
        :type k: int
        :rtype: str
        """
