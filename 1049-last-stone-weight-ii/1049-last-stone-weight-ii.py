class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        
        @cache
        def dfs(index, curStones):
            if index >= len(stones):
                return curStones

            a = dfs(index + 1, stones[index] + curStones)
            b = dfs(index+1, -stones[index] + curStones)

            return min(a if a >= 0 else inf, b if b >= 0 else inf)
        
        return dfs(0, 0)