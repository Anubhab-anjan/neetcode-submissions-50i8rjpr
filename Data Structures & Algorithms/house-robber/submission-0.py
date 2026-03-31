class Solution:
    def rob(self, nums: List[int],dp=None) -> int:
        n= len(nums)
        if dp is None:
            dp = [-1]*(n+1)
        def solve(i):
            if i==0 :
                return 0
            if i==1 :
                return nums[0]
            if dp[i] != -1:
                return dp[i]
            dp[i] = max(nums[i-1]+solve(i-2),solve(i-1))
            return dp[i]
        return solve(n)