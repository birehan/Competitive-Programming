class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        score = 1

        for bracket in s:
            if bracket == ")":
                cur = stack[-1] or 1
                if len(stack) > 1:
                    cur += stack.pop()
                stack[-1] += cur 
            else:
                stack.append(0)

        return stack[0]
