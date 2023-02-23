class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = defaultdict(int)
        left = max_len = 0

        for right, string in enumerate(s):
            if string in dic and dic[string] >= left:
                left = dic[string] + 1
                
            dic[string] = right
            max_len = max(max_len, right-left+1)
        
        return max_len