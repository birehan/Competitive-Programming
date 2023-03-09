# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_width = 1
        if not root:
            return 0
        
        queue = deque([[root, 1]])
        while queue:
            cur_width = queue[-1][1] - queue[0][1] + 1
            max_width = max(max_width, cur_width)

            if cur_width == 1:
                queue[0][1] = 1

            for _ in range(len(queue)):
                cur = queue.popleft()
                
                if cur[0].left:
                    queue.append([cur[0].left, cur[1]*2 - 1])
                
                if cur[0].right:
                    queue.append([cur[0].right, cur[1]*2])
        
        return max_width