from typing import List

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp = [[0, -prices[0]]] + [[[0], [0]] for _ in range(len(prices) - 1)]
        for day in range(1, len(prices)):
            dp[day][0] = max(dp[day-1][0], dp[day-1][1] + prices[day] - fee)
            dp[day][1] = max(dp[day-1][0] - prices[day], dp[day-1][1])
        return max(dp[-1][0], dp[-1][1])