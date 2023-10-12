# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.cost = 0

        def dfs(node):
            if not node:
                return 0
            
            count = node.val - 1
            count += dfs(node.left)
            count += dfs(node.right)
            
            self.cost += abs(count)

            return count

        dfs(root)
        return self.cost