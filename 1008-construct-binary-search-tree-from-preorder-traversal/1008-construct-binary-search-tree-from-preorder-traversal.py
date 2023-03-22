class Solution:
    def helper(self, stack, preorder, index):
        if index == len(preorder):
            return 
        
        cur = TreeNode(preorder[index])

        if preorder[index] < stack[-1].val:
            stack[-1].left = cur
        
        else:
            last = stack[-1]
            while stack and stack[-1].val < preorder[index]:
                last = stack.pop()

            last.right = cur
        
        stack.append(cur)
        self.helper(stack, preorder, index + 1)


    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        stack = [TreeNode(val=inf)]
        self.helper(stack, preorder, 0)
 
        return stack[0].left
        
        