class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        maxP = 0
        for r in range(1,len(prices)):
            profit = prices[r] - prices[l]
            if profit < 0:
                l = r
            maxP = max(maxP,profit)
            r += 1
        return maxP