from collections import defaultdict, deque
def parallelCourses(n, prerequisites):
    # Write your code here.
    graph = defaultdict(list)
    indegree = defaultdict(int)
  
        
    for pre, suf in prerequisites:
        graph[pre].append(suf)
        indegree[suf] += 1
        
    queue = deque()
        
    courses = 0
    for i in range(1, n + 1):
        if indegree[i] == 0:
            courses += 1
            queue.append(i)
  
  
    semsters = 0
    while queue:
        semsters += 1
        for _ in range(len(queue)):
            node = queue.popleft()
            for neighbour in graph[node]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    courses += 1
                    queue.append(neighbour)
        
    if n == courses:
        return indegree
    return -1
