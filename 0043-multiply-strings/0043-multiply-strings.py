class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1=="0" or num2=="0":
            return "0"
        res = [0] * ( len(num1)+ len(num2))

        for n2 in range(len(num2)-1, -1, -1):
            for n1 in range(len(num1)-1, -1, -1):
                index = n1 + n2 + 1
                value = res[index] + int(num1[n1]) * int(num2[n2])
                res[index] = value % 10
                res[index-1] += value // 10

        ans = ""
        for i in res:
            if i or ans: ans += str(i)
        return ans


