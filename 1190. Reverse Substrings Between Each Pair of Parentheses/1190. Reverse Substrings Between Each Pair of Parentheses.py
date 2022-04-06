class Solution(object):
    def reverseParentheses(self, s):

        stack = []
        t = ""
        for i in s:
            if i != ")":
                stack.append(i)
            else:
                word = []
                while stack[-1] != "(":
                    word.append(stack.pop())
                stack.pop()
                for i in word:
                    stack.append(i)
        result = ""
        for i in stack:
            result += i
        return result

        """
        :type s: str
        :rtype: str
        """
