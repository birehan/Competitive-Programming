# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        max_width = 1
        queue = deque([(root, 1)])

        while queue:
            min_val, max_val = inf, -inf
            n = len(queue)

            for _ in range(n):
                node, position = queue.popleft()

                min_val = min(min_val, position)
                max_val = max(max_val, position)

                if node.left:
                    queue.append((node.left, position * 2 - 1))
                
                if node.right:
                    queue.append((node.right, position * 2))
            
            max_width = max(max_width, max_val - min_val + 1)
        
        return max_width


            

        