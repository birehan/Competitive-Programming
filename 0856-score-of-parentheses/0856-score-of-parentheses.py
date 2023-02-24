class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        for bracket in s:
            if bracket == ")":
                value = stack.pop()
                stack[-1] += max( value*2, 1)
            else:
                stack.append(0)

        return stack[0]
