class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        queue = deque([[0, -1]])
        cur_sum = 0
        min_length = inf

        for right, num in enumerate(nums):
            cur_sum += num
            # move from left while greater than k
            while queue and cur_sum - queue[0][0] >= k:
                min_length = min(min_length, right-queue[0][1])
                queue.popleft()

            # pop from right while less
            while queue and queue[-1][0] > cur_sum:
                queue.pop()

            queue.append([cur_sum, right])
        
        return min_length if min_length != inf else -1