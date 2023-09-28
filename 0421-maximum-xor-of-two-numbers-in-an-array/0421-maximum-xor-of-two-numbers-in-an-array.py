class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, value, depth):
        cur = self.root
        for i in range(depth-1, -1, -1):
            if value & (1 << i):
                if cur.one_child == None:
                    cur.one_child = TrieNode()
                cur = cur.one_child
            else:
                if cur.zero_child == None:
                    cur.zero_child = TrieNode()
                
                cur = cur.zero_child

        cur.is_end = True

    def find_pair(self, value, depth):
        cur = self.root
        max_pos = 0
        bits = 0


        for i in range(depth-1, -1, -1):
            if value & (1 << i):
                if cur.zero_child != None:
                    cur = cur.zero_child
                    if cur.is_end:
                        max_pos = max(max_pos, bits)

                elif cur.one_child:
                    bits ^= 1 << i
                    cur  = cur.one_child
                    if cur.is_end:
                        max_pos = max(max_pos, bits)
                else:
                    break
            else:
                
                if cur.one_child != None:
                    bits ^= 1 << i
                    cur = cur.one_child
                    if cur.is_end:
                        max_pos = max(max_pos, bits)

                elif cur.zero_child:
                    cur = cur.zero_child
                    if cur.is_end:
                        max_pos = max(max_pos, bits)
                else:
                    break

    
        return max_pos


class TrieNode:
    def __init__(self):
        self.is_end = False
        self.zero_child = None
        self.one_child = None
    
    
class Solution:
    
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = Trie()
        depth = len(bin(max(nums))) - 2

        for num in nums:
            trie.insert(num, depth)

        ans = 0
        nums.sort()
        for num in nums:
            ans = max(ans, num ^ trie.find_pair(num, depth))
        
        return ans
      
        