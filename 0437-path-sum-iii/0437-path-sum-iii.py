# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root, cur_sum, targetSum):
        if not root:
            return 
        cur_sum += root.val
        self.count += self.dic[cur_sum - targetSum] 
        self.dic[cur_sum] += 1
        
    
        self.helper(root.left, cur_sum, targetSum)
        self.helper(root.right, cur_sum, targetSum)
        self.dic[cur_sum] -= 1

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.dic = defaultdict(int)
        self.dic[0] = 1
        self.count = 0
        self.helper(root, 0, targetSum)

        return self.count