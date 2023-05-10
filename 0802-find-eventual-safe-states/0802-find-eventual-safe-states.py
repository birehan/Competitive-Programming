class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
   
        color = [0] * len(graph)
        answer = set()
        
        def dfs(curNode):
            if color[curNode] == 1: return False
            
            if color[curNode] == 2: return True
            
            color[curNode] = 1
            for neighbor in graph[curNode]:
                if not dfs(neighbor):
                    return False
            
            color[curNode] = 2
            answer.add(curNode)
        
            return True
                
        
        for i in range(len(graph)):
            if color[i] == 0: dfs(i)
                    
        return sorted(list(answer))