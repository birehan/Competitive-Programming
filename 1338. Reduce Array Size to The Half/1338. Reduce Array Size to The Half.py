from collections import Counter


class Solution(object):
    def minSetSize(self, arr):
        length = len(arr) // 2
        arr = Counter(arr)

        li = list(arr.values())
        li.sort()
        result = 0

        while length > 0 and len(li) > 0:
            length -= li.pop()
            result += 1

        return result
        """
        :type arr: List[int]
        :rtype: int
        """
