class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        res = 0
        length = len(piles)//3

        for i in range(length):
            res += piles[-(i+1)*2]
        
        return res
