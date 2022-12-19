# Enter your code here. Read input from STDIN. Print output to STDOUT
import collections
length = int(input())
room_nums = list(map(int, input().split()))
dic = collections.Counter(room_nums)
for k,v in dic.items():
    if v != length:
        print(k)
        break
