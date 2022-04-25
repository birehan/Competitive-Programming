class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k:
            return str(0)
        stack = []
        for i in num:
            while len(stack) > 0 and k > 0 and int(i) < stack[-1]:
                stack.pop()
                k -= 1
            stack.append(int(i))

        while stack and k > 0:
            stack.pop()
            k -= 1

        while len(stack) > 1 and stack[0] == 0:
            stack.pop(0)

        result = ""
        for n in stack:
            result += str(n)

        return result

