# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root):
        if not root:
            return 0, 0
        
        left_sum, left_e = self.helper(root.left)
        right_sum, right_e = self.helper(root.right)

        summ = left_sum + right_sum + root.val
        elements =  left_e + right_e + 1
        if (summ)//elements == root.val:
            self.count += 1

        return summ, elements

    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.count = 0
        self.helper(root)
        return self.count
        