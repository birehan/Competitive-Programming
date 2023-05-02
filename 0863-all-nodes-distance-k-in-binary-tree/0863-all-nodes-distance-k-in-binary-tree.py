# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getStart(self, root, target, level):
        if not root:
            return -1
        if root == target:
            return level

        self.path.append(root)
        res = self.getStart(root.left, target, level+1)
        if res != -1:
            return res

        res = self.getStart(root.right, target, level+1)
        if res != -1:
            return res
        
        self.path.pop()
        return -1
    
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        if k == 0:
            return [target.val]
        
        self.path = []
        

        temp = root
        self.getStart(temp, target, 0)
      
        starter = []
        if self.path:
            starter.append(self.path.pop())
        if target.left:
            starter.append(target.left)
        if target.right:
            starter.append(target.right)



        queue = deque(starter)
        visited = set(starter + self.path)
        visited.add(target)
        level = 0

        while queue:

            length = len(queue)
            level += 1

            if k == level:
                answer = [cur.val for cur in queue]
                return answer

            for _ in range(length):
                cur = queue.popleft()
                if cur and cur.left and cur.left not in visited:
                    queue.append(cur.left)
                    visited.add(cur.left)
                if cur and cur.right and cur.right not in visited:
                    queue.append(cur.right)
                    visited.add(cur.right)
            
            if self.path:
                queue.append(self.path.pop())

       
        return []
        
        
        