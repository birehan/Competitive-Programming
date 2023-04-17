# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        queue = deque([(root, root.val)])
        values = []
        answer = 0
        while queue:
            # print(queue)
            for i in range(len(queue)):
                node, value = queue.popleft()
                if (not node.left and not node.right):
                    answer += int(value )
                if node.left:
                    queue.append((node.left, str(value) + str(node.left.val)))
                if node.right:
                    queue.append((node.right, str(value) + str(node.right.val)))
        
        return answer