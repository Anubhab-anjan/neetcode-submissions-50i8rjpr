class Solution:
    def uniquePaths(self, m: int, n: int,dp=None) -> int:
        if dp is None:
            dp = [[-1]*n for _ in range(m)]
        def solve(i,j):
            if i<0 or j<0:
                return 0
            if i==0 and j==0:
                return 1
            if dp[i][j]!= -1:
                return dp[i][j]
            up = solve(i-1,j)
            left = solve(i,j-1)
            dp[i][j] = up+left
            return dp[i][j]
        return solve(m-1,n-1)     