class Solution:
    def reverseWords(self, s: str) -> str:
        res = ""
        i = len(s)-1
        cur = ""
        while i > -1:
            while i > -1 and s[i] != " ":
                cur += s[i]
                i -= 1
            if cur:
                res += (cur[::-1]) + " "
                cur = ""
            i -= 1
        return res[:-1]
            

                
