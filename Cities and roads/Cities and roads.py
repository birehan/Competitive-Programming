length = int(input())

count = 0
for i in range(length):
    row = list(map(int, input().split()))
    count += sum(row[:i+1])

print(count)

