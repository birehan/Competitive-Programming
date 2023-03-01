class Solution:
    def reverse(self, string):
        return string[::-1]
    
    def invert(self, string):
        inverted = []
        for s in string:
            inverted.append("1" if s=="0" else "0")
        return "".join(inverted)

    def findKthBit(self, n: int, k: int, res="0") -> str:
        if n == 1:
            return res[k-1]
        res = res + "1" + self.reverse(self.invert(res))
        return self.findKthBit(n-1, k, res)

        
    