class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy,sell = 0,0
        lowest_buy = float('inf')
        #highest_sell = float('-inf')
        best_buy = 0
        for i in range(0,len(prices)):
            sell = prices[i]
            #sell = prices[i+1]
            lowest_buy = min(lowest_buy,sell)
            #highest_sell = max(highest_sell,sell)
            profit = sell - lowest_buy
            best_buy = max(best_buy,profit)
        return best_buy
        