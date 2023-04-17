from collections import defaultdict


def biColor(nodes, edges):
    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    
    color = [0] * nodes
    for node in range(1, nodes+1):
        if color[node-1] == 0:
            color[node-1] = 1

        for neighbor in graph[node]:
            if color[neighbor-1] == color[node-1]:
                return False
            
            color[neighbor-1] = -1 * color[node-1]
        
    
    return True


while True:
    nodes = int(input())    
    if nodes == 0:
        break
        
    edgeCount = int(input())
    edges = []

    for _ in range(edgeCount):
        a, b = tuple(map(int, input().split()))
        edges.append([a, b])
    if (biColor(nodes, edges)):
        print("BICOLOURABLE.")
    else:
        print("NOT BICOLOURABLE.")
        




