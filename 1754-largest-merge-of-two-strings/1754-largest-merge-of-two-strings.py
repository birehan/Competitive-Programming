class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        res = []
        w1 = w2 = 0
        length1, length2 = len(word1), len(word2)

        def compare(i, j):
            while i < length1 and j < length2 and word1[i] == word2[j]:
                i += 1
                j += 1
            
            if  i >= length1:
                return 1
            if  j >= length2:
                return 0
            
            return word1[i] < word2[j]
            
            
        while w1 < length1 and w2 < length2:
            if compare(w1, w2):
                res.append(word2[w2])
                w2 += 1
            else:
                res.append(word1[w1])
                w1 += 1
        
        res.extend(word1[w1:])
        res.extend(word2[w2:])
        return "".join(res)