class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        dic = defaultdict(int)
        for index, string in enumerate(s):
            dic[string] = index
        
        stack = []
        res = []
        for index, string in enumerate(s):
            if string not in stack:
                while stack and stack[-1] > string and dic[stack[-1]] > index:
                    stack.pop()
                stack.append(string)

        return "".join(stack)