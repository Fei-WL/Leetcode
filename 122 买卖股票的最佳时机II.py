from typing import List

"""
dp数组的定义：
首先，第一个维度，表示第i天
每个维度都有两个状态：
0状态表示当天交易结束后，手上没有股票了，要转到这个状态，先前一天手上没有股票，那么就依然会是这个状态；先前一天手上有股票，到了第i天卖了
1状态表示当天交易结束后，手上有股票，要转到这个状态，先前一天手上有股票，那么就依然会是这个状态；先前一天没有股票，买了第i天的股票
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0, -prices[0]]] + [[0, 0] for _ in range(len(prices) - 1)]
        for day in range(1, len(prices)):
            dp[day][0] = max(dp[day-1][0], dp[day-1][1] + prices[day])
            dp[day][1] = max(dp[day-1][1], dp[day-1][0] - prices[day])

        return max(dp[-1][0], dp[-1][1])