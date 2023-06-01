# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, node):
        if not node:
            self.dp[node] = 0
            return
        
        self.helper(node.left)
        self.helper(node.right)

        self.dp[node] = max(self.dp[node.left] + self.dp[node.right], node.val + self.parent[node.left] + self.parent[node.right])

        self.parent[node] = self.dp[node.left] + self.dp[node.right]

        

        

    def rob(self, root: Optional[TreeNode]) -> int:
        self.dp = defaultdict(int)
        self.parent = defaultdict(int)
        self.helper(root)

        return self.dp[root]
        