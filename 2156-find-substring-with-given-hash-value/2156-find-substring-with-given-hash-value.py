class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        powers = (power ** (k-1)) % modulo        
        left = 0
        value = 0
        m = len(s)
        s = s[::-1]
        ans = None

        for right in range(m):
            value = ((value * power)% modulo + ((ord(s[right]) - 96)%modulo)) % modulo

            if right - left + 1 == k:
                if value == hashValue:
                    ans = right +1
                   
                value = (value - ((ord(s[left]) - 96)%modulo * powers)) % modulo

                left += 1
        if ans == None:
            return -1
         
        res = s[ans-k:ans]
        return res[::-1]
