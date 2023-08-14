class Solution:
    @cache
    def numTrees(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        
        value = 0
        for i in range(n):
            value += self.numTrees(i) * self.numTrees(n - i -1)
        
        return value
        