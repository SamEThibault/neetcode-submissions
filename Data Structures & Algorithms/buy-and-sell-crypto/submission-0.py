class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        highest = max(prices)

        profit = 0
        for i in range(len(prices) - 1):
            curr_profit = highest - prices[i]
            profit = max(curr_profit, profit)
            if highest == prices[i]:
                highest = max(prices[i+1:])
        return profit
