# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        averageLevels = []
        queue = deque([root])

        while queue:
            levelWidth = len(queue)
            levelSum = 0
            for _ in range(levelWidth):
                cur = queue.popleft()
                levelSum += cur.val

                if cur.left:
                    queue.append(cur.left)

                if cur.right:
                    queue.append(cur.right)
            
            averageLevels.append(levelSum/levelWidth)
        
        return averageLevels