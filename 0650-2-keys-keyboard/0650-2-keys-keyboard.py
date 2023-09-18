class Solution:
    def minSteps(self, n: int) -> int:
        
        @cache
        def dfs(length, copyed):
            if length == n:
                return 0
            
            if length > n:
                return inf
            
            if copyed:
                a = dfs(length + copyed, copyed)
                b = dfs(length + copyed, 0)
                return min(a + 1, b + 1)
            else:
                a = dfs(length + length, length)
                b = dfs(length + length, 0)
                return min(a + 2, b + 2)
        
        return dfs(1, 0)



            

            
