class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = True
        self.count = 0
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        cur = self.root

        for letter in word:
            key = ord(letter) - 97
            if not cur.children[key]:
                cur.children[key] = TrieNode()
            
            cur.children[key].count += 1
            cur = cur.children[key]
        
        cur.is_end = True
    
    def findPrefixScore(self, word):
        cur = self.root
        count = 0

        for letter in word:
            key = ord(letter) - 97
            count += cur.children[key].count
            cur = cur.children[key]
    
        return count
            

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        answer = []
        for word in words:
            answer.append(trie.findPrefixScore(word))
        
        return answer
