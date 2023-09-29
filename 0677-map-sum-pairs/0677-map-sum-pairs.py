class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [None for _ in range(26)]
        self.value = 0


class MapSum:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, key: str, val: int) -> None:
        cur = self.root

        for letter in key:
            key = ord(letter.lower()) - 97
            if cur.children[key] == None:
                cur.children[key] = TrieNode()
            
            cur = cur.children[key]
        
        cur.is_end = True
        cur.value = val

    def checkPrefixExists(self, prefix):
        cur = self.root

        for letter in prefix:
            key = ord(letter.lower()) - 97
            if cur.children[key] == None:
                return False, None

            cur = cur.children[key]

        return True, cur      

    def sum(self, prefix: str) -> int:
        valid, node = self.checkPrefixExists(prefix)
        if not valid:
            return 0
        
        value = 0
        
        stack = [node]
        while stack:
            cur = stack.pop()
            value += cur.value
            
            for child in cur.children:
                if child != None:
                    stack.append(child)
        
        return value

        
