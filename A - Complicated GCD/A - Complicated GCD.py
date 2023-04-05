def find_gcd(num1, num2):
    a,b = num1, num2

    while num2:
        num1, num2 = num2, num1 % num2

    return (num1) if (num1 == 1 or b-a==0 ) else 1

a, b = tuple(map(int, input().split()))
print(find_gcd(a, b))
