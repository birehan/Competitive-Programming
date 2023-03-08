# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        counter = defaultdict(int)

        def helper(root):
            if not root:
                return

            counter[root.val] += 1
            helper(root.left)
            helper(root.right)
        
        helper(root)
        mode = max(counter.values())
        answer = []

        for key, value in counter.items():
            if value == mode:
                answer.append(key)
        
        return answer