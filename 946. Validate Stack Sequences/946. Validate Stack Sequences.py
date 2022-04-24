from typing import List

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:

        stack = []
        pos = 0

        for val in pushed:
            stack.append(val)
            while stack and stack[-1] == popped[pos]:
                stack.pop()
                pos += 1

        return len(stack) == 0
