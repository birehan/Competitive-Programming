from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:

        # keep track of min and max.
        # the minimum end point create the area.

        left = 0
        right = len(height) - 1

        val = 0
        while left < right:
            x = min(height[left], height[right])
            val = max(x * (right - left), val)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return val

