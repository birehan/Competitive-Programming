from cmath import inf
from collections import defaultdict


n = int(input())
for _ in range(n): 
    row, col, ladder = tuple(map(int, input().split()))
    level_cost = list(map(int, input().split()))
    levels  = defaultdict(set)
    costs  = defaultdict(lambda: inf)

    levels[1].add(1)
    levels[row].add(col)

    costs[(1, 1)] = 0
    costs[(row, col)] = inf


    ladders = defaultdict(list)

    for _ in range(ladder):
        start_r, start_c, end_r, end_c, gain = tuple(map(int, input().split()))
        levels[start_r].add(start_c)
        levels[end_r].add(end_c)  
        ladders[start_r].append((start_c, end_r, end_c, gain))

    levels = dict(sorted(levels.items()))
    for level in levels:
        levels[level] = list(levels[level])
        levels[level].sort()


    for level in levels:
        
        for i in range(1, len(levels[level])):
            dist = abs(levels[level][i] - levels[level][i-1])
            costs[(level, levels[level][i])] = min(costs[(level, levels[level][i])], costs[(level, levels[level][i-1])] + (dist * level_cost[level-1]))
        

        for i in range(len(levels[level])-2, -1, -1):
            dist = abs(levels[level][i] - levels[level][i+1])
            costs[(level, levels[level][i])] = min(costs[(level, levels[level][i])], costs[(level, levels[level][i+1])] + (dist * level_cost[level-1]))


        # print(level, ladders[level])

        for start_c, end_r, end_c, gain in ladders[level]:
            costs[(end_r, end_c)] = min(costs[(end_r, end_c)], costs[(level, start_c)] - gain)
      
    if costs[(row, col)] != inf:
        print(costs[(row, col)])
    else:
        print("NO ESCAPE")   
