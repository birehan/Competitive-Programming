class TrieNode:
    def __init__(self):
        self.children = {}
        self.indexes = []


class WordFilter:
    def __init__(self, words: List[str]):
        self.root = TrieNode()
        for index, word in enumerate(words):
            cur = self.root
            n = len(word)

            for i in range(n):
                if (word[i], word[n-i-1]) not in cur.children:
                    cur.children[(word[i], word[n-i-1])] = TrieNode()
                
                cur.children[(word[i], word[n-i-1])].indexes.append(index)
                cur = cur.children[(word[i], word[n-i-1])]

    def f(self, pref: str, suff: str) -> int:
        pre_index, suf_index = 0, len(suff)-1
        queue = deque([self.root])

        while pre_index < len(pref) or suf_index >= 0:

            if pre_index < len(pref) and suf_index >= 0:
                if (pref[pre_index], suff[suf_index]) not in queue[0].children:
                    return -1
                
                queue[0] = queue[0].children[(pref[pre_index], suff[suf_index])]

                pre_index += 1
                suf_index -= 1
            
            elif pre_index < len(pref):
                for _ in range(len(queue)):
                    cur = queue.popleft()
                    for a, b  in cur.children:
                        if a == pref[pre_index]:
                            queue.append(cur.children[(a, b)])
                    
                pre_index += 1

            elif suf_index >= 0:
                for _ in range(len(queue)):
                    cur = queue.popleft()
                    for a, b in  cur.children:
                        if b == suff[suf_index]:
                            queue.append(cur.children[(a, b)])
                    
                suf_index -= 1
                          

        if queue:
            return max([cur.indexes[-1] for cur in queue])
        
        return -1

        



# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)