# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
            
        dic = {0:1}

        def dfs(node, curSum):
        
            count = dic.get(curSum - targetSum, 0)
            dic[curSum] = dic.get(curSum, 0) + 1

            if node.left:
                count += dfs(node.left, curSum + node.left.val)

            if node.right:
                count += dfs(node.right, curSum + node.right.val)
            
            dic[curSum] -= 1
            
            return count

        
        return dfs(root, root.val)
            

        