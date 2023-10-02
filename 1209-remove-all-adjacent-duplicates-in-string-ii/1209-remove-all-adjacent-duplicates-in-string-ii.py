class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack, frequency = [], []

        for string in s:
            if not stack or stack[-1] != string:
                stack.append(string)
                frequency.append(1)
            else:
                frequency[-1] += 1
            
            if frequency[-1] == k:
                stack.pop()
                frequency.pop()
        
        return "".join([stack[i] * frequency[i] for i in range(len(stack))])
        