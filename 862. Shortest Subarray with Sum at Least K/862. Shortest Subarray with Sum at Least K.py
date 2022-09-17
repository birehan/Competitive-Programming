from collections import deque
from typing import List


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        pre_sum = [0]
        queue = deque()
        res = float('inf')

        for i in nums:
            pre_sum.append(i + pre_sum[-1])

        for index, value in enumerate(pre_sum):
            while queue and pre_sum[queue[-1]] >= value:
                queue.pop()

            while queue and value - pre_sum[queue[0]] >= k:
                res = min(res, index - queue.popleft())

            queue.append(index)
        return res if res != float('inf') else -1