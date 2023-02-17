n, m = map(int, input().split())
num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))

res = []
p1, p2 = 0, 0
while p1 < n and p2 < m :
    if num1[p1] < num2[p2]:
        res.append(num1[p1])
        p1 += 1
    else:
        res.append(num2[p2])
        p2 += 1

res.extend(num1[p1: ])
res.extend(num2[p2: ])
print(*res)


