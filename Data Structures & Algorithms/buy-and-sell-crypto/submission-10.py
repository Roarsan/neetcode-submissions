class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprice = 0 
        left = 0
        res = 0
        for right in range(1,len(prices)):

            if prices[left] > prices[right]:
                left = right
            else:
                res = prices[right] - prices[left]
            maxprice = max(res,maxprice)

        return maxprice

        