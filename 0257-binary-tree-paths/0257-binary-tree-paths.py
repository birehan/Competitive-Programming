# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, cur, root):
        if not root:
            return

        cur.append(str(root.val))
        if not root.left and not root.right:
            res = "->".join(cur.copy())
            self.answer.append(res)
            return

        self.helper(cur, root.left)
        if root.left:
            cur.pop()
        self.helper(cur, root.right)
        if root.right:
            cur.pop()
        
        
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        self.answer = []
        self.helper([], root)
        return self.answer







        
