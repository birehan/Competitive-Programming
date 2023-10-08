class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None

        def dfs(node):
            cur_p, cur_q = None, None
            if node == p:
                cur_p = p
            
            if node == q:
                cur_q = q
            
            if node.left:
                a, b = dfs(node.left)
                if a and b:
                    return a, b
                if a == p:
                    cur_p = a
                if b == q:
                    cur_q = b
                
            
            if node.right:
                a, b = dfs(node.right)
                if a and b:
                    return a, b
                if a == p:
                    cur_p = a
                if b == q:
                    cur_q = b
            
            if cur_p and cur_q:
                return node, node
            else:
                return cur_p, cur_q
        
        a, b = dfs(root)
        return a




        