class Solution(object):
    def maxCoins(self, piles):
        if len(piles) == 0:
            return 0

        piles.sort()
        summ = 0
        while len(piles) != 0:
            piles.pop(0)
            piles.pop()
            summ += piles.pop()

        return summ

        """
        :type piles: List[int]
        :rtype: int
        """
