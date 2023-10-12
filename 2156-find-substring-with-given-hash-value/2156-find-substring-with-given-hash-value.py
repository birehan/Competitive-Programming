class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        powers = (power ** (k-1)) % modulo        
        left = value = ans = 0
        s = s[::-1]

        for right in range(len(s)):
            value = ((value * power)% modulo + ((ord(s[right]) - 96)%modulo)) % modulo

            if right - left + 1 == k:
                if value == hashValue:
                    ans = right +1
                   
                value = (value - ((ord(s[left]) - 96)%modulo * powers)) % modulo

                left += 1

        if ans == 0:
            return -1
         
        return s[ans-k:ans][::-1]
