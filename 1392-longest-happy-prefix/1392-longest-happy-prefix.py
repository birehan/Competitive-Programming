class Solution:
    def longestPrefix(self, s: str) -> str:
        pi = [0] * len(s)
        index, pointer = 1, 0

        while index < len(s):
            if s[index] == s[pointer]:
                pi[index] = pointer + 1
                index += 1
                pointer += 1
            elif pointer == 0:
                index += 1
            else:
                pointer = pi[pointer - 1]
        
        return s[:pi[-1]]

        
        


        