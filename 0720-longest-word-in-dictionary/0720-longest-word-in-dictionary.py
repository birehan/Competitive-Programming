class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [None for _ in range(26)]


class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insertWord(self, word):
        cur = self.root

        for letter in word:
            key = ord(letter.lower()) - 97
            if cur.children[key] == None:
                cur.children[key] = TrieNode()
            
            cur = cur.children[key]
        
        cur.is_end = True

        return

    def checkWordExists(self, word):
        cur = self.root

        for letter in word:
            key = ord(letter.lower()) - 97
            if cur.children[key] == None:
                return False

            cur = cur.children[key]

        return cur.is_end


class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        for word in words:
            trie.insertWord(word)


        def dfs(node):
            cur = ""
            for i in range(26):
                if node.children[i] != None and node.children[i].is_end:
                    response = chr(97 + i)
                    response += dfs(node.children[i])
                    if len(cur) < len(response) or (len(cur) == len(response) and response < cur):
                        cur = response
           
            return cur
    

        return dfs(trie.root)
        
      

        