class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        periods, left = len(prices), 0

        for right in range(1, len(prices)):
            if prices[right-1] - prices[right] != 1:
                left = right
            else:
                periods +=  right - left

        return periods

