class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.max_path_sum = -inf
        def dfs(root):
            if not root:
                return 0
                       
            left = dfs(root.left)
            right = dfs(root.right)
            cur_path = max(left, 0) + max(right, 0) + root.val
            self.max_path_sum = max(cur_path, self.max_path_sum)

            return max(left, right, 0) + root.val
        
        dfs(root)
        return self.max_path_sum