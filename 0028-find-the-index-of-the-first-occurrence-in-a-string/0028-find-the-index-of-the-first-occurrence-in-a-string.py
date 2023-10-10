class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        mod = 10 ** 9 + 7
        alpha = 27
        powers = []
        n = len(needle)

        for i in range(n+1):
            powers.append((alpha ** i) % mod)
        
        needle_key = 0
        m = len(haystack)

        for i in range(n):
            
            needle_key += ((powers[n-i-1] % mod * (ord(needle[i]) - 96) % mod) % mod)
            needle_key %= mod
        
        left = 0
        value = 0
        for right in range(m):
            value = ((value * alpha) + ((ord(haystack[right]) - 96)))% mod

            if right - left + 1 == n:
                if value == needle_key:
                    return left
                
                value = (value - ((ord(haystack[left]) - 96) * powers[right-left])) % mod

                left += 1
        
        return -1

            