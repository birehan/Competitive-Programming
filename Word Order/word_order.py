# Enter your code here. Read input from STDIN. Print output to STDOUT
# how many numbers to accept
dic = {}
length = int(input())
for i in range(length):
    cur = input()
    dic[cur] = 1 + dic.get(cur, 0)

print(len(dic.keys()))
for k, v in dic.items():
    print(v, end=" ")
