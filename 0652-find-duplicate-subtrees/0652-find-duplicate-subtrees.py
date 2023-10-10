# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        store = set()
        count = {}

        def dfs(root):
            if not root:
                return tuple([201])
            
            left = dfs(root.left)
            right = dfs(root.right)
            cur =  tuple([root.val]) + left + right

            if cur in store:
                count[cur] = root
            
            store.add(cur)
            return cur
        
        dfs(root)

        return count.values()



        