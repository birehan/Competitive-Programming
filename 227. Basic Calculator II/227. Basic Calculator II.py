import math


class Solution:
    def calculate(self, s: str) -> int:
        if not s: return 0

        s = "".join(s.split())
        stack = []
        op = "+"
        cur_num = ''

        count = 0
        for i in s:
            if i.isdigit():
                cur_num += i

            if not i.isdigit() or count == len(s) - 1:
                if op == "+" or op == "-":
                    stack.append(int(op + cur_num))
                elif op == '*':
                    stack.append(stack.pop() * int(cur_num))
                elif op == "/":
                    stack.append(math.trunc(stack.pop() / int(cur_num)))

                cur_num = ""
                op = i
            count += 1

        return sum(stack)
