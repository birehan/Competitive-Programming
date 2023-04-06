from collections import defaultdict


length = int(input())
grid = []

for _ in range(length):
    row = list(map(int, input().split()))
    grid.append(row)

adjecents = defaultdict(list)

for i in range(length):
    for j in range(length):
        if i != j and grid[i][j]:
            adjecents[i+1].append(j+1)

for value in adjecents.values():
    print(len(value), *value)
