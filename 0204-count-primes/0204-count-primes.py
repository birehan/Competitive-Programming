class Solution:
    def countPrimes(self, n: int) -> int:
        primes = [True] * ((5 * 10**6) + 1)

        index = 2
        count = 0
        while index < n:
            if primes[index]:
                count += 1
                for i in range(index, n, index):
                    primes[i] = False
            
            index += 1
        
        return count

        