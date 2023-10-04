from sys import stdin, stdout
from collections import defaultdict
from math import inf


def inp():
    return int(stdin.readline())


def inlt():
    return list(map(int, stdin.readline().strip().split()))


def insr():
    s = stdin.readline().strip()
    return list(s[:len(s)])


def invr():
    return map(int, stdin.readline().strip().split())

n, m = invr()
edges = []

for _ in range(m):
    a, b, cost = invr()
    edges.append((cost, a, b))


graph = defaultdict(list)

costs = [inf] * ( n + 1)
path = [i for i in range(n+1)]


def find(cur):
    cur_path = []
    unique = set()
    count = 100
    while (len(cur_path) < 2 or path[cur] not in unique) and count:
        count -= 1
        unique.add(path[cur])
        cur_path.append(path[cur])
        cur = path[cur]
    
    index = cur_path.index(path[cur])
    cur_path = cur_path[index:] + [path[cur]]

    
    print("YES")
    print(*cur_path[::-1])
        

for i in range(n):
    for cost, a, b in edges:
        if costs[a] == inf:
            costs[a] = 0

        if costs[a] + cost < costs[b]:
            if i == n -1 :
                (find(b))
                exit()
            costs[b] = costs[a] + cost
            path[b] = a
        

print("NO")
  


    

