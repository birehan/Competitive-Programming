class Solution:
    def maximumSum(self, nums: List[int]) -> int:

        def get_primes(number):
            primes = set()
            start = 2

            while start * start <= number:
                while number and number % start == 0:
                    if start in primes:
                        primes.remove(start)
                    else:
                        primes.add(start)
                    
                    number //= start
                
                start += 1
            
            if number > 1:
                primes.add(number)
            
            if not primes:
                primes.add(1)

            return primes
    
        
        total = defaultdict(int)

        for i in range(len(nums)):
            cur_primes = tuple(list(sorted(get_primes(i+1))))
            total[cur_primes] += nums[i]
        

        return max(total.values())
