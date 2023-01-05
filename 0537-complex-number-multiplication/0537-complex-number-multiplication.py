class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        num1 = num1.split("+")
        a, b = int(num1[0]), int(num1[1][:-1])
        num2 = num2.split("+")
        c, d = int(num2[0]), int(num2[1][:-1])

        real = str(a * c - b * d)
        img = str(a * d + b * c) + "i"  
        return real + "+" + img