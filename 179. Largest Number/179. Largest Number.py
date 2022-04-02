class Solution(object):
    def largestNumber(self, nums):
        result = list(map(str, nums))
        for i in range(len(result)):
            for j in range(i + 1, len(result)):
                if result[i] + result[j] < result[j] + result[i]:
                    result[i], result[j] = result[j], result[i]
        result = str(int("".join(result)))

        return result
        """
        :type nums: List[int]
        :rtype: str
        """
