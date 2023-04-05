class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        primes = [True for _ in range(right+1)]
        
        d = 2
        while d * d <= right:
            if primes[d]:
                for i in range(d*2, right+1, d):
                    primes[i] = False

            d += 1
        min_value = inf
        a, b = None, None
        answer = [-1, -1]
        for i in range(left, right+1):
            if primes[i] and a == None and i > 1:
                a = i
            elif primes[i] and b == None and i > 1:
                b = i
                if min_value > b - a:
                    min_value = b - a
                    answer = [a, b]
                a = b
                b = None

        return answer
       