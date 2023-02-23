class Solution:
    def findAnagrams(seelf, s: str, p: str) -> List[int]:
        res = []
        left = 0
        dic = Counter(p)
        for right in range(len(s)):
            if s[right] in dic:
                dic[s[right]]  -= 1
            
            if right - left + 1 == len(p):
                value = sorted(dic.values())
                if value[0] >= 0 and sum(value) ==0:
                    res.append(left)
                if s[left] in dic:
                    dic[s[left]] += 1
                left += 1

        return res