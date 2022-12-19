# Enter your code here. Read input from STDIN. Print output to STDOUT
happy = 0
n, m = map(int, input().split())
original = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))

for value in original:
    if value in A:
        happy += 1
    if value in B:
        happy -= 1
        
print(happy)
