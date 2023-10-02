class TrieNode:
    def __init__(self):
        self.children = {}
        self.indexes = []


class WordFilter:
    def __init__(self, words: List[str]):
        self.root = TrieNode()
        for i in range(len(words)):
            self.insert(words[i], i)
    
    def insert(self, word, index):
        cur = self.root
        n = len(word)
        for i in range(n):
            pre = word[i]
            post = word[n-i-1]
            if (pre, post) not in cur.children:
                cur.children[(pre, post)] = TrieNode()
            
            cur.children[(pre, post)].indexes.append(index)
        
            cur = cur.children[(pre, post)]
        

    def f(self, pref: str, suff: str) -> int:
        pre_index, suf_index = 0, len(suff)-1
        cur = self.root
        while pre_index < len(pref) and suf_index >= 0:
            if (pref[pre_index], suff[suf_index]) not in cur.children:
                return -1
            
            cur = cur.children[(pref[pre_index], suff[suf_index])]

            pre_index += 1
            suf_index -= 1
        
    
        if pre_index < len(pref):
            queue = deque([cur])

            while queue and pre_index < len(pref):

                for _ in range(len(queue)):
                    cur = queue.popleft()
                    for a, b  in cur.children:
                        if a == pref[pre_index]:
                            queue.append(cur.children[(a, b)])
                    
                pre_index += 1
            
            if queue:
                return max([cur.indexes[-1] for cur in queue])
            
            else:
                return -1
        
        if suf_index >= 0:
            queue = deque([cur])

            while queue and suf_index >=0:

                for _ in range(len(queue)):
                    cur = queue.popleft()
                    for a, b in  cur.children:
                        if b == suff[suf_index]:
                            queue.append(cur.children[(a, b)])
                    
                suf_index -= 1
            
            if queue:
                return max([cur.indexes[-1] for cur in queue])
            else:
                return -1
        

        return cur.indexes[-1]

        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)