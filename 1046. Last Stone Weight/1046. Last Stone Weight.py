from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            y = max(stones)
            stones.remove(y)
            x = max(stones)
            stones.remove(x)

            if x != y:
                y = y - x
                stones.append(y)
        answer = stones[0] if stones else 0
        return answer