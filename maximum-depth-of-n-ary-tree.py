"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        
        depth = 0
        for child in root.children:
            child_depth = self.maxDepth(child)
            depth = max(child_depth, depth)
        
        return depth + 1