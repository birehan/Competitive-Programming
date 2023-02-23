class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dic = defaultdict(int)
        max_len = 0
        left = 0

        for right, string in enumerate(s):
            dic[string] += 1
            while left <= right and (right-left+1) > max(dic.values()) + k:
                dic[s[left]] -= 1
                if not dic[s[left]]:
                    del dic[s[left]]
                left += 1
            
            max_len = max(max_len, right - left + 1)

        return max_len




      