class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        maxProfit = 0
        currentProfit = 0
        for right in range(1,len(prices)):
            num = prices[right]
            if prices[left] > num:
                left = right
            else:
                currentProfit =  num - prices[left]
            maxProfit = max(maxProfit,currentProfit)

        return maxProfit
            


        