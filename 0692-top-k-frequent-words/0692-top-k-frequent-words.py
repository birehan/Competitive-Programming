class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        sortdict = sorted(counter.items(), key=lambda x:[-x[1], x[0]], reverse=True)
        answer = [sortdict[i][0] for i in range(-1, -k-1, -1)]

        return answer