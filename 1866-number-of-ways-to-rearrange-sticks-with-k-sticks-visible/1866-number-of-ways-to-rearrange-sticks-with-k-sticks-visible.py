class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        #Solution 1 - Recursive DP 
        # hmap = {}
        # def dp(n,k):
        #     if n==k:
        #         return 1
        #     if n==0 or k==0:
        #         return 0
        #     if (n,k) in hmap:
        #         return hmap[(n,k)]
        #     hmap[(n,k)] = (dp(n-1,k-1) + (n-1)* dp(n-1,k))%((10**9)+7)
        #     return hmap[(n,k)]
        
        # return dp(n,k)

        #Solution 2 
        MOD = 10**9 + 7
        dp = [[0]*(k+1) for _ in range(n+1)]
        dp[0][0] = 1

        for i in range(1, n+1):
            for j in range(1, k+1):
                dp[i][j] = (dp[i-1][j-1] + (i-1)*dp[i-1][j]) % MOD

        return dp[n][k]