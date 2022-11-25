n, l, r = [int(x) for x in input().split()]
dic = {0: [0], 1: [1]}

def dfs(n):
    if n in dic:
        return dic[n]
    dic[n] = dfs(n//2) + [n%2] + dfs(n//2)
    return dic[n]

part = dfs(n)
array = part + [n % 2] + part
res = 0
for i in range(l, r+1):
    if array[i] == 1:
        res += 1

print(res)