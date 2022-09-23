from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        prefix = {0: 1}
        cur_sum = 0
        for i in nums:
            cur_sum += i

            res += prefix.get(cur_sum - k, 0)
            prefix[cur_sum] = 1 + prefix.get(cur_sum, 0)

        return res