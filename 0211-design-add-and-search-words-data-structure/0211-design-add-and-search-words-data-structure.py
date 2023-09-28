class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [None for _ in range(26)]

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word: str) -> None:
        cur = self.root

        for letter in word:
            key = ord(letter.lower()) - 97
            if cur.children[key] == None:
                cur.children[key] = TrieNode()
            
            cur = cur.children[key]
        
        cur.is_end = True

        return   

    def searchWord(self, word, root):
        if not root:
            return False

        if word == "":
            return root.is_end
       
        key = ord(word[0]) - 97

        if word[0] == ".":
            for child in root.children:
                if child and self.searchWord(word[1:], child):
                    return True
            return False
    
        return self.searchWord(word[1:], root.children[key]) 


    def search(self, word):
        return self.searchWord(word, self.root)


