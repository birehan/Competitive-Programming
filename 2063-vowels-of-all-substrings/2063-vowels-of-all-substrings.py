class Solution:
    def countVowels(self, word: str) -> int:
        count = 0
        for index, letter in enumerate(word):
            if letter in "aeiou":
                count += len(word)
                count += (index) * (len(word) -index -1)

        return count
       