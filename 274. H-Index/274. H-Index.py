from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:

        citations.sort()

        result = 0
        length = len(citations)
        for i in range(len(citations)):
            if citations[i] >= (length - i):
                result = max(length - i, result)

        return result

