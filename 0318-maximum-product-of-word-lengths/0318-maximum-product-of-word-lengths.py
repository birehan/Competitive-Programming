class Solution:
    def compute_bit(self, word):
        value = 0
        off_set = 97

        for letter in word:
            index = ord(letter) - off_set
            value |= 1 << index
        
        return value

    def maxProduct(self, words: List[str]) -> int:
        max_len = 0
        values = []
        for word in words:
            values.append(self.compute_bit(word))

        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if not (values[i] & values[j]):
                    max_len = max(max_len, len(words[i]) * len(words[j]))

        return max_len