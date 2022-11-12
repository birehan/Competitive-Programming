class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in s:
            if i != "]":
                stack.append(i)
            else:
                cur = ""
                count = ""
                while stack and stack[-1] != "[":
                    cur = stack.pop() + cur
                stack.pop()
                while stack and stack[-1].isdigit():
                    count = stack.pop() + count

                stack.append(cur * int(count))

        return "".join(stack)













