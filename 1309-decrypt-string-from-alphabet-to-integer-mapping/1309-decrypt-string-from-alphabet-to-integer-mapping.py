class Solution:
    def freqAlphabets(self, s: str) -> str:
        letter_base = 96
        res = ""
        index = len(s)-1
        while index >= 0:
            if s[index] == "#":
                cur = s[index-2] + s[index-1]
                res += chr(letter_base + int(cur))
                index -= 3
            else:
                res += chr(letter_base + int(s[index]))
                index -= 1
        
        return res[::-1]

        