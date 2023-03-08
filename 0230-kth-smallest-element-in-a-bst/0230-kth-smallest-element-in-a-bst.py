# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:  
    def helper(self, root, k):
        if not root:
            return 0
    
        left = self.helper(root.left, k)
        if  left + 1 == k and self.value == -1:
            self.value = root.val
            return 0

        right = self.helper(root.right, k - left-1)
        
        return left + right + 1

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.value = -1            
        self.helper(root, k)
        return self.value

