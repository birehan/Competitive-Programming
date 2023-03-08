# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def calculate(self, root , row , col):
        if not root:
            return

        self.dic[col].append((row, root.val)) 
        self.calculate(root.left,row + 1,col - 1)
        self.calculate(root.right , row + 1, col + 1)
        
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        self.dic = defaultdict(list)
        self.calculate(root , 0 , 0)
        answer = list(dict(sorted(self.dic.items())).values())

        for i in range(len(answer)):
            answer[i] = [j for (i, j) in sorted(answer[i])]

        return answer      

  

        