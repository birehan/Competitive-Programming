n, m = map(int, input().split())
num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))

count = [0] * m
index = 0
for i in range(m):
    while index < n and num1[index] < num2[i]:
        index += 1
    count[i] = index

print(*count)
