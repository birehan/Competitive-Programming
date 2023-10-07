# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        
        answer = []
        path = defaultdict(list)
        path[root].append(root.val)
        queue = deque([(root, root.val)])

        while queue:
            node, curSum = queue.popleft()

            if curSum == targetSum and not node.left and not node.right:
                answer.append(path[node])
            
            if node.left :
                path[node.left] = path[node] + [node.left.val]
                queue.append((node.left, curSum + node.left.val))
            
            if node.right :
                path[node.right] = path[node] + [node.right.val]
                queue.append((node.right, curSum + node.right.val))
        
        return answer
        