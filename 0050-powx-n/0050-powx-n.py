class Solution:
    def myPow(self, x: float, n: int) -> float:

        answer = count = 1
        cur = x
        times = abs(n)
        while times > 0:
            if count * 2 < times:
                cur *= cur
                count *= 2
            else:
                answer *= cur
                cur = x
                times -= count
                count = 1
        return answer if n > 0 else 1/answer
