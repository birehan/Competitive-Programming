class Solution:
    def maxAreaOfIsland(self, grid):
   
       
        def checkFourDir(val):
            ans = []
            dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for d in dir:
                
                possible = [val[0] + d[0], val[1] + d[1]]
                if 0 <= possible[0] < len(grid) and 0 <= possible[1] < len(grid[0]):
                    if grid[possible[0]][possible[1]] == 1:
                        ans.append(possible)
            
            return ans
        
   
        
        is_visited = []
        def connectedLength(n,is_connected):
            is_connected.append(n)
            is_visited.append(n)
            connected_list = checkFourDir(n)
            for i in connected_list:
                if i not in is_connected:
                    connectedLength(i, is_connected)
            return len(is_connected)
                
        
        def helper():
            result = 0
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 1:
                        if [i, j] not in is_visited:
                            result = max(result, connectedLength([i, j], []))
            return result
        
        return helper()
                                            
    
        """
        :type grid: List[List[int]]
        :rtype: int
        """