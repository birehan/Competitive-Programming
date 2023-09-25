class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        
        @cache
        def dfs(index, multi):
            if index >= len(satisfaction):
                return 0
            
            a = (multi * satisfaction[index]) + dfs(index + 1, multi + 1)
            b = dfs(index + 1, multi)

            return max(a, b)
        
        return dfs(0, 1)
        
