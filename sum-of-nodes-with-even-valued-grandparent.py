# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.summ = 0
        def dfs(root, parent, grandParent):
            if not root:
                return
            
            if parent and grandParent:
                if grandParent % 2 == 0:
                    self.summ += root.val

            if parent != None:            
                grandParent = parent

            
            parent = root.val
            dfs(root.left, parent, grandParent)
            dfs(root.right, parent, grandParent)
        
        dfs(root, None, None)
        return self.summ