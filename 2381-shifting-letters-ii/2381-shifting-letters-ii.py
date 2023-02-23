class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix = [0] * (len(s)+1)

        for a, b, direc in shifts:
            prefix[a] += 1 if direc else -1
            prefix[b+1] += 1 if not direc else -1
        
        ans = []
        cur = 0
        for i in range(len(s)):
            cur += prefix[i]
            letter = (ord(s[i]) - ord("a") + cur)%26
            ans.append(chr(letter + ord('a')))
        
        return "".join(ans)
