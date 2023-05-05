class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        pair = defaultdict(list)

        for key, freq in counter.items():
            pair[-freq].append(key)
        
        pair = list(pair.items())
        heapify(pair)
        answer = []

        while pair and len(answer) < k:
            freq, items = heappop(pair)
            heapify(items)
            
            while len(answer) < k and items:
                answer.append(heappop(items))
        
        return answer


        

        

