# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        if not root:
            return []
        

        def dfs(node):
            if not node:
                return []
            
            val = node.val
            store = []
            if node.left and node.left.val in to_delete:
                hold = node.left
                node.left = None
                store.extend(dfs(hold))
            else:
                store.extend(dfs(node.left))
            
            if node.right and node.right.val in to_delete:
                print(node.val, node.right.val)
                hold = node.right
                node.right = None
                store.extend(dfs(hold))
            else:
                store.extend(dfs(node.right))
            
            if node.val in to_delete:
                if node.left and node.left.val not in to_delete:
                    store.append(node.left)
                if node.right and node.right.val not in to_delete:
                    store.append(node.right)

            print(val, store)
            return store
        
        nodes = dfs(root)
        if root.val not in to_delete:
            nodes.append(root)
        
        return nodes

            