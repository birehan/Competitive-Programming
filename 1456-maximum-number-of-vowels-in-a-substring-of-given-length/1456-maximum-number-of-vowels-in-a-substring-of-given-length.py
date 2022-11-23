class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ["a", "e", "i", "o", "u"]
        vowel_count = max_vowel = 0
        left = 0
        for right, letter in enumerate(s):
            if letter in vowels:
                vowel_count += 1

            if right-left+1 == k:
                max_vowel = max(max_vowel, vowel_count)
                if s[left] in vowels:
                    vowel_count -= 1
                left += 1   

        return max_vowel     