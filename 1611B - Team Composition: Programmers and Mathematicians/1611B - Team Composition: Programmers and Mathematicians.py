length = int(input())

for _ in range(length):
    a, b = tuple(map(int, input().split()))
    min_value = min(a, b)
    max_pair = min((a+b)//4, min_value)
    print(max_pair)
 
