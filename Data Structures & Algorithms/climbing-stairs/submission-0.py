class Solution:
    def climbStairs(self, n: int,dp=None) -> int:
        if dp is None:
            dp = [-1]*(n+1)
        if (n==0 or n==1 ):
            return 1
        if dp[n] != -1:
            return dp[n]
        dp[n] = self.climbStairs(n-1,dp)+self.climbStairs(n-2,dp)
        return dp[n]