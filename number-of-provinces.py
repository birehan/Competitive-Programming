class Solution:
    def dfs(self, node):
        if node in self.visited:
            return
        
        self.visited.add(node)
        for neighbor in self.adjecents[node]:
            self.dfs(neighbor)

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        self.adjecents = defaultdict(list)
        size = len(isConnected)

        for i in range(size):
            for j in range(size):
                if isConnected[i][j]:
                    self.adjecents[i].append(j)
                    self.adjecents[j].append(i)
            
        
        self.visited = set()
        provinces = 0
        for node in range(size):
            if node not in self.visited:
                provinces += 1
                self.dfs(node)
        
        return provinces