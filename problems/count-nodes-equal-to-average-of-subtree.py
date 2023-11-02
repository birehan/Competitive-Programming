# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            if not node:
                return 0, 0, 0
            
            length_l, total_l, count_l = dfs(node.left)
            length_r, total_r, count_r  = dfs(node.right)

            total = total_l + total_r + node.val
            length = length_l + length_r + 1
            count = count_l + count_r

            if total//length == node.val:
                count += 1
            
            return length, total, count
    

        _, _, count = dfs(root)
        return count

            
        