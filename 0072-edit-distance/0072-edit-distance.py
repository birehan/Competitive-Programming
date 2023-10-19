class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dirs = [[0, 1], [1, 0], [1, 1]]

        @cache
        def dfs(i, j):
            if i >= len(word1):
                return len(word2) - j
            
            if j >= len(word2):
                return len(word1) - i
            
            cost = inf
            if word1[i] != word2[j]:
                for r, c in dirs:
                    cost = min(cost, dfs(r + i, c + j))
                return cost + 1
            else:
                return dfs(i + 1, j + 1)
        
        return dfs(0, 0)
            
            
        