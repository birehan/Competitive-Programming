class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split()
        s = sorted(s, key=lambda x: x[-1])
        return " ".join(x[:-1] for x in s)

