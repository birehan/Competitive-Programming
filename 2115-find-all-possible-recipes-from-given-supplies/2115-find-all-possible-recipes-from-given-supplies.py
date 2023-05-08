class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        source = set(recipes)
        degree = defaultdict(int)
        
        supplies = set(supplies)
        graph = defaultdict(list)
        for i in range(len(recipes)):
            for j in range(len(ingredients[i])):
                if ingredients[i][j] not in supplies:
                    graph[ingredients[i][j]].append(recipes[i])
                    degree[recipes[i]] += 1
                    if recipes[i] in source:
                        source.remove(recipes[i])
                
                
       
        queue = deque(list(source))
        answer = []
        
        while queue:
            cur = queue.popleft()
            answer.append(cur)
            for neghibor in graph[cur]:
                degree[neghibor] -= 1
                if degree[neghibor] == 0:
                    queue.append(neghibor)
        
        return answer
            