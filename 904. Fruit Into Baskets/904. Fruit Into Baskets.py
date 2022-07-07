from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_count = 0
        left = 0
        right = 0
        dic = {}
        while right < len(fruits):
            dic[fruits[right]] = right
            if len(dic) > 2:
                min_val = min(dic.values())
                del dic[fruits[min_val]]
                left = min_val + 1

            max_count = max(max_count, right - left + 1)
            right += 1

        return max_count