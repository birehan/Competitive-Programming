from collections import Counter
 
def helper(string, nums):
    dic = {}
    for s, n in zip(string, nums):
        if n in dic and dic[n] != s:
            return False
        dic[n] = s
 
    return True
 
n = int(input())
 
for _ in range(n):
    length = int(input())
    nums = list(map(int, input().split()))
    string = input()
    if helper(string, nums):
        print("YES")
    else:
        print("NO")
