import operator


class Solution(object):
    def evalRPN(self, tokens):
        if len(tokens) == 0:
            return 0

        stack = []
        for v in tokens:
            if v.isnumeric() or (v.startswith("-") and v != "-"):
                stack.append(int(v))
            else:
                x = stack.pop()
                y = stack.pop()
                if v == "+":
                    stack.append(y + x)
                elif v == "-":
                    stack.append(y - x)
                elif v == "*":
                    stack.append(y * x)
                elif v == "/":
                    div = int(operator.truediv(y, x))
                    stack.append(div)
        return stack[0]

        """
        :type tokens: List[str]
        :rtype: int
        """
