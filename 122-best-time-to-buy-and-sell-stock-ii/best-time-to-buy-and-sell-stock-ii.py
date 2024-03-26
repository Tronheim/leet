class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = 0
        for n in range(len(prices) - 1):
            if prices[n] < prices[n + 1]:
                profits += prices[n + 1] - prices[n]
        return profits