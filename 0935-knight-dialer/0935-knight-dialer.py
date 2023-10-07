class Solution:
    def knightDialer(self, n: int) -> int:
        
        num_map = {1: [6, 8], 2: [7, 9], 3:[4, 8], 4:[0, 3, 9], 5:[], 6:[0, 1, 7], 7:[2, 6], 8:[1, 3], 9: [2, 4], 0: [4, 6]}

        @cache
        def dfs(num, rem):
            if rem == 0:
                return 1
            

            count = 0
            if rem == n:
                for i in range(10):
                    count += dfs(i, rem -1)
            else:
                for child in num_map[num]:
                    count += dfs(child, rem - 1)
            
            return count
        
        return dfs(0, n) % (10**9 + 7)