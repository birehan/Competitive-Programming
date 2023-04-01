length = int(input())   

for _ in range(length):
    a = int(input())
    b = a & -a

    while a ==b or not(a & b):
        b += 1

    print(b)
