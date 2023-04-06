from collections import defaultdict
edges = defaultdict(list)

def AddEdge(u, v):
    edges[u].append(v)
    edges[v].append(u)

def Vertex(u):
    print(*edges[u])


length = int(input())
operations = int(input())

for _ in range(operations):
    values = list(map(int, input().split()))
    if values[0] == 1:
        AddEdge(values[1], values[2])
    else:
        Vertex(values[1])

