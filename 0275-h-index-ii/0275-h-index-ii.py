class Solution:
    def hIndex(self, citations: List[int]) -> int:
        res = 0
        length = len(citations)
        left, right = -1, length

        while right > left + 1:
            mid = (left + right)//2
            if citations[mid] >= length - mid:
                right = mid
                res = length - mid
            else:
                left = mid

        return res