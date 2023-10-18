class Solution:
    def countVowels(self, word: str) -> int:
        dp = 0
        total = 0

        for i in range(len(word)):
            if word[i] in "aeiou":
                dp = (dp + 1 *(i+1))
            
            total += dp

        return total
     