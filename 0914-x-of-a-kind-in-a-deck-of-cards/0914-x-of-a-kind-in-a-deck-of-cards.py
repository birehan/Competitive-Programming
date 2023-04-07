class Solution:
    def factorize(self, num):
        factors = set()
        d =2 

        while d * d <= num:
            while num % d == 0:
                factors.add(d)
                num //= d
            d += 1
        if  num > 1:
            factors.add(num)
        return factors

    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck) < 2:
            return False

        count = list(set(Counter(deck).values()))
        freq = self.factorize(count[0])
        
        for i in range(1, len(count)):
            cur = self.factorize(count[i])
            freq = freq.intersection(cur)
            if not freq:
                return False

        
        return True












        