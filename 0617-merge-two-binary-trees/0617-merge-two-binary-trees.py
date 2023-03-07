# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 or not root2:
            return root1 or root2
    
        cur_sum = (root1.val ) + (root2.val)
        dummy = TreeNode(val=cur_sum)
       
        dummy.left = self.mergeTrees(root1.left, root2.left)
        dummy.right = self.mergeTrees(root1.right, root2.right)

        return dummy