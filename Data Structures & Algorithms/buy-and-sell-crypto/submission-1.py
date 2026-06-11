class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        max_profit = 0

        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
                r = l + 1
            else:
                curr_profit = prices[r] - prices[l]
                if curr_profit > max_profit:
                    max_profit = curr_profit
                r += 1
        
        return max_profit
        