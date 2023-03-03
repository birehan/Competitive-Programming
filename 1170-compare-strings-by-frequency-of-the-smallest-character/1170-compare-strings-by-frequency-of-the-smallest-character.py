class Solution:
    def find_value(self, value, words):
        left, right = -1, len(words)
        while right > left + 1:
            mid = (right + left) // 2
            if words[mid] > value:
                right = mid
            else:
                left = mid
        return len(words)-right

    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        for i in  range(len(queries)):
            counter = Counter(queries[i])
            counter = sorted(counter.items())
            queries[i] = counter[0][1]
        
        for i in  range(len(words)):
            counter = Counter(words[i])
            counter = sorted(counter.items())
            words[i] = counter[0][1]

        words.sort()

        res = []
        for q in queries:
            res.append(self.find_value(q, ((words))))
        
        return res
