class Solution:
    def similarPairs(self, words: List[str]) -> int:
        dic = {}
        total = 0

        for word in words:
            word = "".join(sorted(set(word)))
            prev = dic.get(word, 0)
            total += prev
            dic[word] = 1 + prev
       
        
        return total
        

        