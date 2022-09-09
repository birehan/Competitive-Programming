import heapq
from collections import Counter
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)

        dic = Counter(tasks)
        maxHeap = [-i for i in dic.values()]
        heapq.heapify(maxHeap)

        queue = []
        time = 0

        while maxHeap or queue:
            time += 1
            if maxHeap:
                cur_time = 1 + heapq.heappop(maxHeap)
                if cur_time:
                    queue.append([cur_time, time + n])
            if queue and queue[0][1] == time:
                heapq.heappush(maxHeap, queue.pop(0)[0])
        return time