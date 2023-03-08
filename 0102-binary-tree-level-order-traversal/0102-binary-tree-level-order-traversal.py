# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        answer = []
        store = deque([root])

        while store:
            cur_ans = []

            for _ in range(len(store)):
                cur = store.popleft()
                cur_ans.append(cur.val)

                if cur.left:
                    store.append(cur.left)
                if cur.right:
                    store.append(cur.right)
            
            answer.append(cur_ans)         
        
        return answer 

