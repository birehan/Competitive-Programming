class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_dic = Counter(s[:len(p)-1])
        p_dic = Counter(p)
        result = []
        left = 0
        for right in range(len(p)-1, len(s)):
            s_dic[s[right]] = 1 + s_dic.get(s[right], 0)
            if s_dic == p_dic:
                result.append(left)
            s_dic[s[left]] -= 1
            if s_dic[s[left]] == 0:
                del s_dic[s[left]]
            left += 1
        
        return result

      
        



      