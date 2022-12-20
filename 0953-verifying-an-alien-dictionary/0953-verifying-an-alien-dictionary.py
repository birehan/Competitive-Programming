class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic = {}
        letter = 97
        for i in order:
            dic[i] = chr(letter)
            letter += 1
        
        def convert(word):
            res = "".join([dic[i] for i in word])
            return res


        for i in range(len(words)):
            words[i] = convert(words[i])
        
        return sorted(words) == words