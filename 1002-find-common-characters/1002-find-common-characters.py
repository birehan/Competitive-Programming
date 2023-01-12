class Solution:

    def helper(self, word):
            arr = [0] * 26
            offset = ord("a")
            for i in word:
                index = ord(i) - offset
                arr[index] += 1
            return arr

    def commonChars(self, words: List[str]) -> List[str]:
        
        first = self.helper(words[0])
        offset = ord("a")

        for i in range(1, len(words)):
            arr = self.helper(words[i])
            for i in range(len(arr)):
                first[i] = min(first[i], arr[i])
        
        common_chr = []

        for i in range(len(first)):
            cur = [chr(offset+i)] * first[i]
            common_chr.extend(cur)
        
        return common_chr




       