class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        buy = sell = profit = 0
        

        for value in prices:
            if  buy and sell and (value + fee <= sell):
                profit += sell - buy - fee
                buy = sell = 0

            if not buy or value < buy:
                buy = value
            elif (not sell and (value - buy - fee) > 0) or (sell and value > sell):
                sell = value

        if buy and sell:
            profit += sell - buy - fee


        return profit
            
            
        # stack 
        # [1, 8,]
        