class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        index = 0
        res = ""
        while index < len(word1) and index < len(word2):
            res += word1[index] + word2[index]
            index += 1
        
        res += word1[index:] + word2[index:]
        return res
      