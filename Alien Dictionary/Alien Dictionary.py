#User function Template for python3
from collections import deque, defaultdict

class Solution:
    def findUnique(self, word1, word2):
    
        for i in range(len(word1)):
            if i < len(word2) and word1[i] != word2[i]:
                return word1[i], word2[i]
        
        return "", ""
        
        
    def findOrder(self,alien_dict, N, K):
        graph = defaultdict(list)
        Indegree = defaultdict(int)
        
        alien_dict = list(alien_dict)
        shift = 97
        source = set([chr(shift+i) for i in range(K)])
        
        for i in range(1, len(alien_dict)):
            left, right = self.findUnique(alien_dict[i-1], alien_dict[i])
            if left:
                graph[right].append(left)
                Indegree[left] += 1
                if left in source:
                    source.remove(left)
        
        answer = []
        
        queue = deque(list(source))

        while queue:
            cur = queue.popleft()
            answer.append(cur)
            for child in graph[cur]:
                Indegree[child] -= 1
                if Indegree[child] == 0:
                    queue.append(child)
        
        answer.reverse()
      
        return "".join(answer)
