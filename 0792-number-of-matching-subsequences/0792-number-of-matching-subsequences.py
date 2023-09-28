class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        store = defaultdict(list)
        for i in range(len(s)):
            store[s[i]].append(i)
        
        count = 0
        for word in words:
            last_ind = 0
            cur_count = 1
            for letter in word:
                index = bisect_left(store[letter], last_ind)
                if index >= len(store[letter]):
                    cur_count = 0
                    break
                
                last_ind = store[letter][index] + 1
                

            count += cur_count
        
        return count
        