# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
dic = defaultdict(list)
n, m = map(int, input().split())

for i in range(n):
    cur = "".join(input().split())
    if cur in dic:
        dic[cur].append(str(i+1))
    else:
        dic[cur] = [str(i+1)]

for i in range(m):
    cur = "".join(input().split())
    if cur in dic:
        print(" ".join(dic[cur]))
    else:
        print(-1)

