class Solution:
    def dfs(self, node,adjecents, color):
        if not color[node]:
            color[node] = 1

        answer = True
    
        for neghibor in adjecents[node]:
            if color[neghibor] == color[node]:
                return False
            
            if color[neghibor]:
                continue

            color[neghibor] = -1 * color[node]
            answer = answer and self.dfs(neghibor,adjecents, color)

        return answer
            

    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adjecents = defaultdict(list)
        for ai, bi in dislikes:
            adjecents[ai].append(bi)
            adjecents[bi].append(ai)
        
        color = [0] * (n + 1)
        for i in range(1, n+1):
            if not color[i] and not self.dfs(i, adjecents, color):
                return False

        return True