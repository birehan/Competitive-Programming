class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        string = ""
        for c in s:

            if c in string:
                index = 0
                while c != string[index]:
                    index += 1
                string = string[index + 1:]

            if c not in string:
                string += c

            if len(string) > longest:
                longest = len(string)
        return longest