class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        max_gain = 0

        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            
            max_gain = max(max_gain,  prices[i] - buy)
        
        return max_gain
        