class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        current = 0 
        right = 1
        for right in range(len(prices)):

            if prices[right] <= prices[current]:
                current = right
            else:
                sellPrice = prices[right] - prices[current]      
                profit = max(profit,sellPrice)


        return profit



        