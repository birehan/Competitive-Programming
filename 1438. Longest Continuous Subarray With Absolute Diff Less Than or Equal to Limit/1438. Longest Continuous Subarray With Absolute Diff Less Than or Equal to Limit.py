from collections import deque
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_q, max_q = deque(), deque()
        res = 1
        l = 0

        for i, v in enumerate(nums):
            while min_q and min_q[-1] > v:
                min_q.pop()
            min_q.append(v)
            while max_q and max_q[-1] < v:
                max_q.pop()
            max_q.append(v)

            if max_q[0] - min_q[0] <= limit:
                res = max(res, i - l + 1)
            else:
                if min_q[0] == nums[l]:
                    min_q.popleft()
                if max_q[0] == nums[l]:
                    max_q.popleft()
                l += 1
        return res
