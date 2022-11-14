class Solution:
    def myPow(self, x: float, n: int) -> float:

        def power(n, count, res, answer):
            if n == 0:
                return answer
            if count * 2 < n:
                return power(n, count*2, res*res, answer)
            else:
                return power(n-count, 1, x, answer*res)
            
        answer  = power(abs(n), 1, x, 1) 
        return answer if n > 0 else 1/answer