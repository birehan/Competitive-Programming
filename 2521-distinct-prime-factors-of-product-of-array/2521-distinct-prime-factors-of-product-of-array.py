class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        destinct_primes = set()

        for num in nums:
            
            d = 2
            while d * d <= num:
                while num % d == 0:
                     destinct_primes.add(d)
                     num //= d
                d += 1
            
            if num > 1:
                destinct_primes.add(num)

        return len(destinct_primes)
