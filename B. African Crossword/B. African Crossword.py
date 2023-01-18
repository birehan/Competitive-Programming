from collections import defaultdict

def helper(grid, row, col):
    dic_row = defaultdict(int)
    dic_col = defaultdict(int)
    for r in range(row):
        for c in range(col):
            dic_row[(r, grid[r][c])] += 1
            dic_col[(c, grid[r][c])] += 1

    ans = []
    for r in range(row):
        for c in range(col):
            if dic_row[(r, grid[r][c])] < 2 and dic_col[(c, grid[r][c])] < 2:
                ans.append(grid[r][c])
                
    return "".join(ans)

size = list(map(int, input().split()))
grid = []
for i in range(size[0]):
    grid.append(list(input()))

print(helper(grid, size[0], size[1]))    

