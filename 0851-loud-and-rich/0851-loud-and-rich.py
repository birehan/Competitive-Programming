class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:

        graph = defaultdict(list)
        source = set([i for i in range(len(quiet))])
        answer = [i for i in range(len(quiet))]
        Indegree = defaultdict(int)

        for a, b in richer:
            graph[a].append(b)
            if b in source:
                source.remove(b)
            Indegree[b] += 1 
        queue = deque(source)

        while queue:
            cur_index = queue.popleft()
            for child in graph[cur_index]:
                Indegree[child] -= 1
                if quiet[answer[cur_index]] < quiet[answer[child]]:
                    answer[child] = answer[cur_index]
                    
                if Indegree[child] == 0:
                    queue.append(child)
        
        return answer

                 
            
           