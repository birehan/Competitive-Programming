# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.ans = None

        def dfs(root):
            if self.ans or not root:
                return 
            
            dfs(root.left)

            if self.k == 1:
                self.ans = root.val
                self.k -= 1
                return

            self.k -= 1
            dfs(root.right)
        
        dfs(root)
        return self.ans
        
        