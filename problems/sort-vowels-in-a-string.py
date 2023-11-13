class Solution:
    def sortVowels(self, s: str) -> str:
        s = list(s)
        vowels = []
        for index, string in enumerate(s):
            if string in "aeiouAEIOU":
                vowels.append(string)
                s[index] = "_"

        vowels.sort()
        ind = 0

        for index,string in enumerate(s):
            if string == "_":
                s[index] = vowels[ind]
                ind += 1
        
        return "".join(s)
