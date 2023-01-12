from collections import defaultdict

def helper(grid):
    row, col = len(grid), len(grid[0])

    diagonal1 = defaultdict(int)
    diagonal2 = defaultdict(int)
    
    for r in range(row):
        for c in range(col):
            diagonal1[r-c] += grid[r][c]
            diagonal2[r+c] += grid[r][c]

    max_sum = float('-inf')
    for r in range(row):
        for c in range(col):
            cur =  diagonal1[r-c] + diagonal2[r+c] - grid[r][c]
            max_sum = max(max_sum, cur)
    return max_sum
    
length = int(input())

for _ in range(length):
    size = list(map(int, input().split()))
    grid = []
    
    for i in range((size[0])):
        row = list(map(int, input().split()))
        grid.append(row)
    
    print(helper(grid))
