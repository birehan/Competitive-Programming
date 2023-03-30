class Solution:
    def findComplement(self, num: int) -> int:
        index = 1
        while index <= num:
            index <<= 1
        
        return (index - 1) ^ num