class Solution:
    def splitString(self, s: str, prev="", index=0) -> bool:
        if index == len(s) and  prev != s:
            return True
        
        cur = ""
        for i in range(index, len(s)):
            cur += s[i]
            if not prev or int(prev) - int(cur) == 1:
                 if self.splitString(s, cur, i+1):
                     return True

            elif int(prev) < int(cur):
                return False
        