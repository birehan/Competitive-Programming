class Solution:
    def countGoodNumbers(self, n: int) -> int:

        mod = (10**9 + 7)

        def power(a, n):
            answer = 1

            while n > 0:
                if (n & 1):
                    answer  = (answer * a) % mod
                    
                a = (a * a) % mod
                n >>= 1
            
            return answer


        return (power(5, ceil(n/2)) * power(4, floor(n/2))) % mod
      