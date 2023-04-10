# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        stack = []
        def dfs(root):
            if not root:
                return
            
            stack.append(str(root.val))
            if root.left or root.right:
                stack.append("(")
                dfs(root.left)
                stack.append(")")
            
            if root.right:
                stack.append("(")
                dfs(root.right)
                stack.append(")")

        dfs(root)
        return "".join(stack)