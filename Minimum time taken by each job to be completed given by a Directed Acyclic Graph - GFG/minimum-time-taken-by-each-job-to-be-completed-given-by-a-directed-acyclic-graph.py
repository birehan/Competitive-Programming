from typing import List
from collections import deque, defaultdict


from typing import List


class Solution:
    def minimumTime(self, n : int,m : int, edges : List[List[int]]) -> int:
        graph = defaultdict(list)
        Indegree = defaultdict(int)
        visited = set([i for i in range(1, n+1)])
        
        for a, b in edges:
            graph[a].append(b)
            Indegree[b] += 1
            
            if b in visited:
                visited.remove(b)
        
        queue = deque(list(visited))
        answer = [1 for i in range(n)]
        
      
        time = 0
        
        while queue:
            time += 1
            for _ in range(len(queue)):
                cur = queue.popleft()
                answer[cur-1] = str(time)
                for child in graph[cur]:
                    Indegree[child] -= 1
                    
                    if Indegree[child] == 0 and child not in visited:
                        visited.add(child)
                        queue.append(child)
            
        
        return " ".join(answer)
            
        # code here
        



#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()



class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        a=IntArray().Input(2)
        
        
        edges=IntMatrix().Input(a[1], a[1])
        
        obj = Solution()
        res = obj.minimumTime(a[0],a[1], edges)
        
        print(res)
        

# } Driver Code Ends