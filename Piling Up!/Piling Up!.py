# Enter your code here. Read input from STDIN. Print output to STDOUT
blocks = int(input())
values = []
for i in range(blocks):
    length = int(input())
    value = list(map(int, input().split()))
    values.append((length, value))

for length, value in values:
    left, right = 0, length - 1
    valid = "Yes"
    prev = float('inf')
    while left < right:
        if value[left] >= value[right] and value[left] <= prev:
            prev = value[left]
            left += 1
        elif value[right] >= value[left] and value[right] <= prev:
            prev = value[right]
            right -= 1
        else:
            valid = "No"
            break
    print(valid)
            
