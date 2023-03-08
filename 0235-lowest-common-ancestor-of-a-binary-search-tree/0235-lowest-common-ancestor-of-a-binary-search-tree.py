# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if (root == p or root==q) or list(sorted([root.val, p.val, q.val]))[1] == root.val:
            return root

        if (p.val < root.val):
           return self.lowestCommonAncestor(root.left, p, q)
        
        return self.lowestCommonAncestor(root.right, p, q)
