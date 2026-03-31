from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        # extra space for i+2 access
        dp = [[0] * 2 for _ in range(n+2)]

        for i in range(n-1, -1, -1):
            # can buy
            dp[i][1] = max(-prices[i] + dp[i+1][0], dp[i+1][1])
            # holding stock (must sell or skip)
            dp[i][0] = max(prices[i] + dp[i+2][1], dp[i+1][0])

        return dp[0][1]
