class Solution:
    def minCostClimbingStairs(self, cost: List[int],dp=None) -> int:
        n = len(cost)
        if dp is None:
            dp = [-1]*(n+1)
        def solve(i):
            if i==0 or i==1:
                return 0
            if dp[i] != -1:
                return dp[i]
            dp[i] = min(cost[i-1]+solve(i-1),cost[i-2]+solve(i-2))
            return dp[i]
        return solve(n)