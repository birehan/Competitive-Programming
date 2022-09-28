from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        indices = []
        count = 0
        for i in range(len(nums)):
            if nums[i] % 2 != 0:
                indices.append(i)

        l, r = 0, k - 1
        while r < len(indices):
            l1 = indices[l]
            l1 -= (indices[l - 1] + 1) if l > 0 else 0

            r1 = (- indices[r] - 1)
            r1 += indices[r + 1] if r + 1 < len(indices) else len(nums)

            count += 1 + l1 + r1 + (l1 * r1)

            l += 1
            r += 1
        return count