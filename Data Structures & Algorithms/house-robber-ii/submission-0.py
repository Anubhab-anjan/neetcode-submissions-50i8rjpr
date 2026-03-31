class Solution:
    def rob(self, nums: List[int], dp=None) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        def robLinear(arr):
            m = len(arr)
            dp = [-1] * (m+1)

            def solve(i):
                if i == 0:
                    return 0
                if i == 1:
                    return arr[0]
                if dp[i] != -1:
                    return dp[i]
                dp[i] = max(arr[i-1] + solve(i-2), solve(i-1))
                return dp[i]

            return solve(m)

        return max(robLinear(nums[:-1]), robLinear(nums[1:]))
