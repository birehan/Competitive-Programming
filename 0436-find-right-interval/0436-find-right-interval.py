class Solution:
    def binary(self, intervals, end):
        left, right = -1, len(intervals)
        while right > left + 1:
            mid = (left + right)//2
            if intervals[mid][0] >= end:
                right = mid
            else:
                left = mid
        return intervals[right][2] if right != len(intervals) else -1

    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        answer = [0] * len(intervals)

        for i in range(len(intervals)):
            intervals[i].append(i)
        
        intervals.sort()
        for start, end, index in intervals:
            answer[index] = self.binary(intervals, end)

        return answer
        