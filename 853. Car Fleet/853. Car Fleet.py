from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        dic = {}
        for i in range(0, len(position)):
            dic[position[i]] = speed[i]
        pos = sorted(dic, reverse=True)
        stack = []
        for i in pos:
            cur_time = (target - i) / dic[i]
            if not stack or cur_time > stack[-1]:
                stack.append(cur_time)

        return len(stack)
