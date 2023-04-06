from collections import defaultdict


length = int(input())
grid = []
for _ in range(length):
    row = list(map(int, input().split()))
    grid.append(row)

in_degree = defaultdict(int)
out_degree = defaultdict(int)

for i in range(length):
    for j in range(length):
        if i != j and grid[i][j]:
            out_degree[i+1].append(j+1)
            in_degree[j+1].append(i+1)


source, sink = [], []

for i in range(length):
    if not in_degree[i+1]:
        source.append(i+1)
    
    if not out_degree[i+1]:
        sink.append(i+1)

print(len(source), *source)
print(len(sink), *sink)




